#contador de vocales
def contador_de_vocales(palabra):
    contador = 0
    for i in palabra:
        contador +=1
    return print('La cantidad de palabras es: ', contador)
palabra = input('Ingrese la palabra a contar')
contador_de_vocales(palabra
                    )