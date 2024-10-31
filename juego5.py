import random
import time

def simon_dice():
    colores = ["rojo", "azul", "verde", "amarillo"]
    secuencia = []

    print("¡Bienvenido a Simón Dice!")
    while True:
        color_nuevo = random.choice(colores)
        secuencia.append(color_nuevo)
        
        print("\nSecuencia:")
        for color in secuencia:
            print(color)
            time.sleep(0.5)
            print("\033[H\033[J", end="")  # Limpia la pantalla

        intento = input("Repite la secuencia (separa los colores con espacios): ").lower().split()
        if intento == secuencia:
            print("¡Correcto!")
        else:
            print("Incorrecto. La secuencia era:", ' '.join(secuencia))
            break

simon_dice()
