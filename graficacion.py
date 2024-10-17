import numpy as np
import matplotlib.pyplot as plt

# Función para graficar múltiples funciones
def graficar_funciones(funciones, x_range=(-10, 10), num_puntos=1000):
    # Crear un array de valores de x en el rango dado
    x = np.linspace(x_range[0], x_range[1], num_puntos)
    
    # Configurar la figura de la gráfica
    plt.figure(figsize=(8, 6))

    # Graficar cada función
    for funcion in funciones:
        y = funcion(x)
        plt.plot(x, y, label=funcion.__name__)
    
    # Añadir título y etiquetas a los ejes
    plt.title("Gráfico de funciones")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    
    # Añadir leyenda para identificar las funciones
    plt.legend()
    
    # Mostrar la cuadrícula
    plt.grid(True)
    
    # Mostrar la gráfica
    plt.show()

# Definir algunas funciones matemáticas
def cuadratica(x):
    return x ** 2

def seno(x):
    return np.sin(x)

def exponencial(x):
    return np.exp(x)

# Llamar a la función para graficar
funciones = [cuadratica, seno, exponencial]
graficar_funciones(funciones)
