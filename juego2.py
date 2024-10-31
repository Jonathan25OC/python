import random

def mezclar_palabra(palabra):
    letras = list(palabra)
    random.shuffle(letras)
    return ''.join(letras)

def juego_atrapador_palabras():
    palabras = ["python", "programacion", "juego", "computadora", "teclado", "raton", "monitor"]
    palabra_secreta = random.choice(palabras)
    palabra_mezclada = mezclar_palabra(palabra_secreta)

    print("¡Bienvenido al Atrapador de Palabras!")
    print("Adivina la palabra correcta de esta mezcla de letras:")
    print(palabra_mezclada)

    intentos = 3
    while intentos > 0:
        adivinanza = input("¿Cuál es la palabra?: ").lower()
        if adivinanza == palabra_secreta:
            print("¡Correcto! Adivinaste la palabra.")
            break
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")
    else:
        print(f"Lo siento, te has quedado sin intentos. La palabra era '{palabra_secreta}'.")

juego_atrapador_palabras()
