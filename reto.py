import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Definir la función objetivo
def objective(x):
    return x[0]*2 + x[1]**2 + x[2]*2 + 12 * (x[0] - 50) + 12 * (x[0] + x[1] - 50)

# Definir las restricciones
def constraint1(x):
    return x[0] - 50

def constraint2(x):
    return x[0] + x[1] - 100

def constraint3(x):
    return x[0] + x[1] + x[2] - 150

# Definir las cotas
bnds = [(50, None), (0, None), (0, None)]

# Definir las restricciones como diccionarios
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3}
cons = [con1, con2, con3]

# Valor inicial
x0 = [50, 50, 50]

# Resolver el problema
solution = minimize(objective, x0, bounds=bnds, constraints=cons)

# Resultados de la optimización
x = solution.x
print('Número de frigoríficos a producir en el primer mes: ', x[0])
print('Número de frigoríficos a producir en el segundo mes: ', x[1])
print('Número de frigoríficos a producir en el tercer mes: ', x[2])
print('Costo mínimo: ', solution.fun)

# Visualización
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Crear una cuadrícula de puntos
X1 = np.linspace(50, 200, 150)
X2 = np.linspace(0, 150, 150)
X1, X2 = np.meshgrid(X1, X2)
X3 = 150 - X1 - X2

# Evaluar la función objetivo
Z = objective([X1, X2, X3])

# Graficar la función objetivo
ax.plot_surface(X1, X2, Z, cmap='viridis', alpha=0.6)

# Graficar la solución óptima
ax.scatter(x[0], x[1], objective(x), color='red', s=100, label='Solución Óptima')

# Graficar las restricciones
x1 = np.linspace(50, 200, 150)
ax.plot(x1, 100 - x1, 0, color='blue', label='$x_1 + x_2 \geq 100$')
ax.plot(x1, 150 - x1, 0, color='green', label='$x_1 + x_2 + x_3 \geq 150$')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('Costo')
ax.legend()

plt.show()