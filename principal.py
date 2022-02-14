from funciones import *

campeones=leer_json("champions.json")

menu='''
1. Listar Campeones
2. Contar Campeones con mas de 550 hp
3. Mostrar estadistica de campeón
0. Salir'''

print(menu)
opcion=int(input("Seleccione opción [0-5]"))
while opcion != 0:
    if opcion == 1:
        for campeon in (listar_campeones(campeones)):
            print (campeon)
    if opcion == 2:
        vida=int(input("Vida mínima: "))
        print(contar_campeon_550hp(campeones,vida))
    if opcion == 3:
        nombre=input("Nombre del campeón: ")
        print(mostrar_estadistica(campeones,nombre))
    else:
        print("Opción incorrecta")

    opcion=int(input("Seleccione opción [0-5]"))      