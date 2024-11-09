# Programa de Inventario

# Diccionario para almacenar el inventario
inventario = {}

# Funciones del programa

def agregar_producto(nombre, cantidad):
    """Agrega un producto al inventario o actualiza su cantidad si ya existe."""
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        inventario[nombre] = cantidad
    print(f"Producto '{nombre}' agregado con cantidad {cantidad}.")

def eliminar_producto(nombre):
    """Elimina un producto del inventario."""
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")

def actualizar_producto(nombre, cantidad):
    """Actualiza la cantidad de un producto en el inventario."""
    if nombre in inventario:
        inventario[nombre] = cantidad
        print(f"Producto '{nombre}' actualizado a cantidad {cantidad}.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")

def ver_inventario():
    """Muestra todos los productos y sus cantidades en el inventario."""
    if inventario:
        print("Inventario actual:")
        for producto, cantidad in inventario.items():
            print(f"- {producto}: {cantidad}")
    else:
        print("El inventario está vacío.")

# Menú principal

def menu():
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Ver inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            agregar_producto(nombre, cantidad)
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = int(input("Nueva cantidad del producto: "))
            actualizar_producto(nombre, cantidad)
        elif opcion == "4":
            ver_inventario()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
