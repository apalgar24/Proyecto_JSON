import json

#Leer fichero JSON
def leer_json(fichero):
    try:
        with open(fichero) as f: 
            campeones=json.load(f)
        return campeones
    except:
        print("Error al leer el fichero :C")

#Listar todos ls campeones registrados
def listar_campeones(campeones):
    lista=[]
    for campeon in campeones:
        lista.append(campeon.get("name"))
    return lista

#Contar campeones que tienen mas de 550 hp
def contar_campeon_hp(campeones,vida):
    lista=[]
    for campeon in campeones:
        if campeon.get("stats").get("hp") >= vida:
            lista.append(campeon.get("name"))
    return len(lista)

#Buscar campeon y mostrar estadística
def mostrar_estadistica(campeones,nombre):
    lista1=[]
    for campeon in campeones:
        if campeon.get("name") == nombre:
            for clave,valor in campeon.get("stats").items():
                lista2=[]
                lista2.append(clave)
                lista2.append(valor)
                lista1.append(lista2)
    return lista1

#Buscar por clase
def buscar_clases(campeones,clase):
    lista=[]
    for campeon in campeones:
        for c in campeon.get("tags"):
            if c == clase:
                lista.append(campeon.get("name"))
    return lista
                
#Sumar estadisticas de campeones
def sumar_estadisticas(campeones,nombre):
    sum=0
    for campeon in campeones:
        if campeon.get("name") == nombre:
            for valor in campeon.get("stats").values():
                sum=sum+valor
    return sum

#Mostrar clases

def mostrar_clases(campeones):
    lista=[]
    for campeon in campeones:
        for clase in campeon.get("tags"):
            if clase not in lista:
                lista.append(clase)
    return lista