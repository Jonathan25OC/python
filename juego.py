import random

def juego_adivinanza():
    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100.")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            adivinanza = int(input("Intenta adivinar el número: "))
            intentos += 1
            if adivinanza < numero_secreto:
                print("Muy bajo. Intenta de nuevo.")
            elif adivinanza > numero_secreto:
                print("Muy alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

juego_adivinanza()
