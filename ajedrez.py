def imprimir_tablero(tamaño=8, caracter1='#', caracter2=' '):
    for fila in range(tamaño):
        for columna in range(tamaño):
            # Alternar entre los dos caracteres según la posición
            if (fila + columna) % 2 == 0:
                print(caracter1, end='')
            else:
                print(caracter2, end='')
        print()  # Salto de línea al terminar una fila.

# Solicitar personalización al usuario
tamaño = int(input("Introduce el tamaño del tablero (ejemplo: 8): "))
caracter1 = input("Introduce el primer carácter (ejemplo: '#'): ")
caracter2 = input("Introduce el segundo carácter (ejemplo: ' '): ")

# Llama a la función con los parámetros personalizados
imprimir_tablero(tamaño, caracter1, caracter2)
