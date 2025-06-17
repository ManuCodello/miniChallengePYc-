#diccionario apartir de dos listas dadas

lista1 = ["Manu", "Jorge", "Antonella", "Penelope"]
años = ["22", "23", "25", "26",]

def creador_diccionarios(clave, valor):
    diccionario = {}
    for i, j in zip(clave, valor):
        diccionario[i] = j
    return diccionario

diccionario = creador_diccionarios(lista1, años)
print(diccionario)  

