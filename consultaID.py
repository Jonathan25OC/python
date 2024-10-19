# Base de datos de productos
productos = {
    "001": {"nombre": "Camisa", "precio": 20, "cantidad": 50},
    "002": {"nombre": "Pantalón", "precio": 30, "cantidad": 40},
    "003": {"nombre": "Zapatos", "precio": 50, "cantidad": 20},
    "004": {"nombre": "Gorra", "precio": 15, "cantidad": 30}
}

# Función para consultar el producto por su ID
def consultar_producto_por_id(id_producto):
    if id_producto in productos:
        producto = productos[id_producto]
        print(f"Producto encontrado: \nNombre: {producto['nombre']}\nPrecio: ${producto['precio']}\nCantidad disponible: {producto['cantidad']}")
    else:
        print("El producto con ese ID no existe.")

# Ejemplo de uso
id_producto = input("Ingrese el ID del producto que desea consultar: ")
consultar_producto_por_id(id_producto)
