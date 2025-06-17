#ordenar lista 
lista_ordenar = [5, 2, 8, 1, 9, 4, 7, 3, 6]
                # [2, 5, 1, 8, 4, 7, 3, 6, 9]
                # [2, 1, 5, 4, 7, 3, 6, 8, 9]

def ordenar_lista(lista):
    while True:
        hubo_cambio = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i] , lista[i + 1] = lista[i + 1], lista[i]
                hubo_cambio = True
                print(lista)
        if not hubo_cambio:
            break
    return lista 
lista_ordenada = ordenar_lista(lista_ordenar)
print("Lista ordenada:", lista_ordenada)


