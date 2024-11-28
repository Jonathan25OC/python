from prettytable import PrettyTable

# Crear una tabla con PrettyTable
tabla = PrettyTable()
tabla.field_names = ["Operador", "Descripción", "Ejemplo", "Resultado"]

# Operadores aritméticos y ejemplos
operadores = [
    ("+", "Suma", "5 + 3", 5 + 3),
    ("-", "Resta", "5 - 3", 5 - 3),
    ("*", "Multiplicación", "5 * 3", 5 * 3),
    ("/", "División", "5 / 3", 5 / 3),
    ("//", "División entera", "5 // 3", 5 // 3),
    ("%", "Módulo (resto)", "5 % 3", 5 % 3),
    ("**", "Potencia", "5 ** 3", 5 ** 3),
]

# Llenar la tabla con los datos
for operador, descripcion, ejemplo, resultado in operadores:
    tabla.add_row([operador, descripcion, ejemplo, resultado])

# Mostrar la tabla
print(tabla)
