import random
import time

def juego_memoria():
    print("Juego de memoria: recuerda la secuencia.")
    secuencia = []

    while True:
        numero_nuevo = random.randint(0, 9)
        secuencia.append(numero_nuevo)
        print("Secuencia:", ' '.join(map(str, secuencia)))
        
        time.sleep(1)
        print("\033[H\033[J", end="")  # Limpia la pantalla

        intento = input("Introduce la secuencia: ")
        if intento == ''.join(map(str, secuencia)):
            print("¡Correcto!")
        else:
            print("Incorrecto. La secuencia era:", ' '.join(map(str, secuencia)))
            break

juego_memoria()
