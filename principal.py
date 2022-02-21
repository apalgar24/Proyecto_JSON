from funciones import *
import time

campeones=leer_json("champions.json")

menu='''
1. Listar Campeones
2. Contar Campeones con vida mínima [400-700]
3. Mostrar estadistica de campeón
4. Mostrar todas las clases
5. Buscar campeón por clase
6. Sumar estadisticas
0. Salir'''

print(menu)
opcion=int(input("Seleccione opción [0-6]"))
while opcion != 0:
    if opcion == 1:
        for campeon in (listar_campeones(campeones)):
            print (campeon)
    elif opcion == 2:
        vida=int(input("Vida mínima: "))
        contar=contar_campeon_hp(campeones,vida)
        if contar == 0:
            print("No hay ningún campeón con vida mínima de",vida,"hp")
        else:
            print("Hay",contar,"campeones con esa vida mínima")
    elif opcion == 3:
        nombre=input("Nombre del campeón: ")
        if len(mostrar_estadistica(campeones,nombre)) == 0:
            print("No existe el campeón")
        else:
            for i in (mostrar_estadistica(campeones,nombre)):
                for stats in i:
                    print(stats,":",end="")
                print()
    elif opcion==4:
        for clase in mostrar_clases(campeones):
            print (clase)
    elif opcion == 5:
        clase=input("Clase: ")
        if len(buscar_clases(campeones,clase)) == 0:
            print("No existe esa clase")
        else:
            for campeon in (buscar_clases(campeones,clase)):
                print(campeon)
    elif opcion ==6:
        nombre=input("Nombre de campeón: ")
        if sumar_estadisticas(campeones,nombre) == 0:
            print("Ese campeón no existe")
        else:
            print("Poder total de",nombre,":",sumar_estadisticas(campeones,nombre))
    else:
        print("Opción incorrecta")
    
    time.sleep(2.5)
    print(menu)
    opcion=int(input("Seleccione opción [0-6]"))      