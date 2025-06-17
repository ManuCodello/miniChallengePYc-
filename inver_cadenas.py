
def invert_cadenas():
    palabras = input("Escriba la cadena a invertir")
    lista_invertida = ""
    for i in range(len(palabras) - 1, -1, -1):  
        lista_invertida += palabras[i]
        
    return print(lista_invertida)  
    
invert_cadenas()


