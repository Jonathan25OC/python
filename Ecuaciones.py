import numpy as np

def newton_raphson(f, df, x0, tol=1e-7, max_iter=100):
    """
    Método de Newton-Raphson para encontrar la raíz de una función no lineal.
    
    Parámetros:
    f: función a la que queremos encontrar la raíz
    df: derivada de la función f
    x0: valor inicial
    tol: tolerancia para el criterio de parada
    max_iter: número máximo de iteraciones
    
    Retorna:
    La raíz encontrada y el número de iteraciones realizadas
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            return x, i
        if dfx == 0:
            raise ValueError("Derivada es cero. El método de Newton-Raphson falla.")
        x = x - fx / dfx
    raise ValueError("Número máximo de iteraciones alcanzado. El método no converge.")

# Ejemplo de uso
# Definimos la función y su derivada
f = lambda x: x**3 - 6*x**2 + 11*x - 6
df = lambda x: 3*x**2 - 12*x + 11

# Valor inicial
x0 = 3.5

# Llamamos a la función
root, iterations = newton_raphson(f, df, x0)

print(f"La raíz encontrada es: {root}")
print(f"Se necesitaron {iterations} iteraciones")
