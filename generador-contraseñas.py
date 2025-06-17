#generador de contraseñas aleatorias entre 8 y 16 caracteres
import random

def generar_contrasena(longitud):
    if longitud < 8 or longitud > 16:
        return("La longitud de la contraseña debe estar entre 8 y 16 caracteres.")
    lista_completa = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-',
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^',
    '_', '`', '{', '|', '}', '~'
    ]
    contador = 0
    contraseña = ""
    while contador < longitud:
        letra = random.choice(lista_completa)
        contraseña += letra
        contador += 1
    return contraseña

generar = generar_contrasena(12) 
print("Contraseña generada:", generar)


            
        
    