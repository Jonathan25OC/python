import random

def juego_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    
    while True:
        jugador = input("Elige 'piedra', 'papel' o 'tijera' (o escribe 'salir' para terminar): ").lower()
        if jugador == "salir":
            print("¡Gracias por jugar!")
            break
        elif jugador not in opciones:
            print("Opción no válida. Intenta nuevamente.")
            continue
        
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")
        
        if jugador == computadora:
            print("Empate.")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("Perdiste.")
        print()

juego_piedra_papel_tijera()
