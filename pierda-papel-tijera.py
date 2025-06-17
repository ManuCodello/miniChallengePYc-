
import random

opciones = ["piedra", "papel", "tijeras"]

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "¡Empate!"
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "tijeras" and computadora == "papel") or \
         (jugador == "papel" and computadora == "piedra"):
        return "Ganaste!"
    else:
        return "Perdiste!"

jugador = input("Elige piedra, papel o tijeras: ").lower()


if jugador not in opciones:
    print("Opción inválida. Elegí bien.")
else:
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    resultado = determinar_ganador(jugador, computadora)
    print(resultado)
