import numpy as np

# Crear dos matrices
matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Suma de matrices
suma = np.add(matriz1, matriz2)

# Resta de matrices
resta = np.subtract(matriz1, matriz2)

# Multiplicación de matrices (elemento a elemento)
multiplicacion_elemento = np.multiply(matriz1, matriz2)

# Multiplicación de matrices (producto matricial)
multiplicacion_matrices = np.dot(matriz1, matriz2)

# Transposición de una matriz
transpuesta = np.transpose(matriz1)

# Imprimir resultados
print("Matriz 1:")
print(matriz1)

print("\nMatriz 2:")
print(matriz2)

print("\nSuma de matrices:")
print(suma)

print("\nResta de matrices:")
print(resta)

print("\nMultiplicación elemento a elemento:")
print(multiplicacion_elemento)

print("\nMultiplicación matricial:")
print(multiplicacion_matrices)

print("\nTranspuesta de la Matriz 1:")
print(transpuesta)
