# Diccionario para almacenar los productos
inventario = {
    "producto_1": {"nombre": "Camisa", "precio": 20, "cantidad": 50},
    "producto_2": {"nombre": "Pantalón", "precio": 30, "cantidad": 40}
}

# Funciones para gestionar el inventario
def agregar_producto(codigo, nombre, precio, cantidad):
    inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}

def actualizar_producto(codigo, cantidad):
    if codigo in inventario:
        inventario[codigo]["cantidad"] += cantidad
    else:
        print("El producto no existe en el inventario.")

def eliminar_producto(codigo):
    if codigo in inventario:
        del inventario[codigo]
    else:
        print("El producto no existe.")

def mostrar_inventario():
    for codigo, detalles in inventario.items():
        print(f"Código: {codigo} | Nombre: {detalles['nombre']} | Precio: ${detalles['precio']} | Cantidad: {detalles['cantidad']}")

# Ejemplo de uso
agregar_producto("producto_3", "Zapatos", 50, 20)
actualizar_producto("producto_1", -5)  # Vendimos 5 camisas
mostrar_inventario()
eliminar_producto("producto_2")
mostrar_inventario()
