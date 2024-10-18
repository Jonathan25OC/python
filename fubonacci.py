# Ejercicio 5: Secuencia de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("¿Cuántos números de la secuencia de Fibonacci quieres ver?: "))
fibonacci(n)
