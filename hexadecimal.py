def convertir_a_hexadecimal():
    try:
        numero = int(input("Ingresa un número decimal: "))
        hexadecimal = hex(numero)
        print(f"El número {numero} en hexadecimal es {hexadecimal[2:].upper()}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Ejecución del programa
convertir_a_hexadecimal()
