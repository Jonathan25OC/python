import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Definición de las restricciones y la función objetivo
c = [-100, -200]  # Coeficientes de la función objetivo (negativos para maximizar)
A = [[4, 2], [8, 8], [0, 2]]  # Coeficientes de las desigualdades
b = [16, 16, 10]  # Términos independientes de las desigualdades

# Resolver el problema usando el método simplex primal
res = linprog(c, A_ub=A, b_ub=b, method='simplex')

# Extraer la solución
X1_opt, X2_opt = res.x
Z_opt = -res.fun  # Cambiar el signo para obtener el valor máximo de Z

# Impresión de los resultados en pasos como en la presentación

print("PASO 1")
print("Convertir las inecuaciones en ecuaciones")
print("4X1 + 2X2 = 16  (Ecuación 1)")
print("8X1 + 8X2 = 16  (Ecuación 2)")
print("2X2 = 10       (Ecuación 3)\n")

print("PASO 2")
print("Identificar los puntos en las gráficas")
print("Ecuación 1: 4X1 + 2X2 = 16")
print("Puntos de intersección con los ejes: (4,0) y (0,8)")
print("Ecuación 2: 8X1 + 8X2 = 16")
print("Puntos de intersección con los ejes: (2,0) y (0,2)")
print("Ecuación 3: 2X2 = 10")
print("Punto de intersección con el eje X2: (0,5)\n")

print("PASO 3")
print("Los puntos son:")
print("A(0,0)")
print("B(2,0)")
print("C(0,2)\n")

print("PASO 4")
print("El valor máximo se alcanza para el punto C(X2 = 2)")
print(f"Z = 400\n")

print(f"Solución óptima (método simplex primal): X1 = {X1_opt}, X2 = {X2_opt}, Z = {Z_opt}")

# Representación gráfica
x1 = np.linspace(0, 5, 400)
x2_1 = (16 - 4 * x1) / 2
x2_2 = (16 - 8 * x1) / 8
x2_3 = 10 / 2

plt.plot(x1, x2_1, label=r'$4X1 + 2X2 \leq 16$')
plt.plot(x1, x2_2, label=r'$8X1 + 8X2 \leq 16$')
plt.axhline(y=x2_3, color='r', linestyle='--', label=r'$2X2 \leq 10$')

# Rellenar la región factible
plt.fill_between(x1, 0, np.minimum(np.minimum(x2_1, x2_2), x2_3), where=(x1 >= 0), color='gray', alpha=0.5)

# Puntos de intersección
A = (0, 0)
B = (2, 0)
C = (0, 2)

# Puntos en la gráfica
plt.scatter(*A, color='red')
plt.scatter(*B, color='red')
plt.scatter(*C, color='red')

plt.text(A[0], A[1], 'A(0, 0)', fontsize=12, verticalalignment='bottom')
plt.text(B[0], B[1], 'B(2, 0)', fontsize=12, verticalalignment='bottom')
plt.text(C[0], C[1], 'C(0, 2)', fontsize=12, verticalalignment='bottom')

# Solución óptima
plt.scatter(X1_opt, X2_opt, color='blue')
plt.text(X1_opt, X2_opt, f'Optimal({X1_opt:.2f}, {X2_opt:.2f})', fontsize=12, verticalalignment='bottom')

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Método gráfico')
plt.legend()
plt.grid(True)
plt.show()