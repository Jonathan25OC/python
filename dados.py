import random

def tirar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def jugar_a_los_dados():
    print("¡Bienvenido al juego de los dados!")
    while True:
        respuesta = input("¿Quieres tirar los dados? (s/n): ").lower()
        if respuesta == 's':
            dado1, dado2 = tirar_dados()
            total = dado1 + dado2
            print(f"Tiraste un {dado1} y un {dado2}. Total: {total}")
            if dado1 == dado2:
                print("¡Doble! ¡Buen tiro!")
        elif respuesta == 'n':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print("Respuesta no válida, por favor ingresa 's' para sí o 'n' para no.")

# Iniciar el juego
jugar_a_los_dados()
