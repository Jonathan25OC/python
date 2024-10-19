# Base de datos de productos
productos = {
    "001": {"nombre": "Camisa", "precio": 20},
    "002": {"nombre": "Pantalón", "precio": 30},
    "003": {"nombre": "Zapatos", "precio": 50}
}

# Factura
factura = []

# Funciones para la facturación
def agregar_a_factura(codigo, cantidad):
    if codigo in productos:
        producto = productos[codigo]
        factura.append({"producto": producto["nombre"], "precio": producto["precio"], "cantidad": cantidad})
    else:
        print("Producto no encontrado.")

def calcular_total(impuesto=0.15):
    subtotal = sum(item["precio"] * item["cantidad"] for item in factura)
    total_impuesto = subtotal * impuesto
    total = subtotal + total_impuesto
    return subtotal, total_impuesto, total

def mostrar_factura():
    print("Factura:")
    for item in factura:
        print(f"{item['cantidad']}x {item['producto']} - ${item['precio']} cada uno")
    subtotal, total_impuesto, total = calcular_total()
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Impuesto: ${total_impuesto:.2f}")
    print(f"Total: ${total:.2f}")

# Ejemplo de uso
agregar_a_factura("001", 2)  # 2 camisas
agregar_a_factura("002", 1)  # 1 pantalón
mostrar_factura()
