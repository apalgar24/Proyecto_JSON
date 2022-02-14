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
def contar_campeon_550hp(campeones,vida):
    lista=[]
    for campeon in campeones:
        if campeon.get("stats").get("hp") >= vida:
            lista.append(campeon.get("name"))
    return len(lista)

#Buscar campeon y mostrar estadística
def mostrar_estadistica(campeones,nombre):
    for campeon in campeones:
        if campeon.get("name") == nombre:
            estadisticas=campeon.get("stats")
    return estadisticas
