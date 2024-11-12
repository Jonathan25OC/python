import threading
import time

def funcion_hilo_1():
    for i in range(5):
        print(f"Hilo 1 - Iteración {i+1}")
        time.sleep(1)  # Pausa de 1 segundo

def funcion_hilo_2():
    for i in range(5):
        print(f"Hilo 2 - Iteración {i+1}")
        time.sleep(1.5)  # Pausa de 1.5 segundos

# Crear los hilos
hilo1 = threading.Thread(target=funcion_hilo_1)
hilo2 = threading.Thread(target=funcion_hilo_2)

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("¡Ambos hilos han terminado!")
