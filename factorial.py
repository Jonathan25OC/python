# Ejercicio 3: Factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("Ingresa un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}")
