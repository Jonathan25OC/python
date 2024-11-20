class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class PuntoDeVenta:
    def __init__(self):
        self.productos = {}
        self.carrito = []

    def agregar_producto(self, codigo, nombre, precio):
        self.productos[codigo] = Producto(nombre, precio)

    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for codigo, producto in self.productos.items():
            print(f"Código: {codigo} | Producto: {producto.nombre} | Precio: ${producto.precio:.2f}")

    def agregar_al_carrito(self, codigo, cantidad):
        if codigo in self.productos:
            producto = self.productos[codigo]
            self.carrito.append((producto, cantidad))
            print(f"Agregado {cantidad}x {producto.nombre} al carrito.")
        else:
            print("El código del producto no existe.")

    def mostrar_carrito(self):
        print("\nCarrito actual:")
        total = 0
        for producto, cantidad in self.carrito:
            subtotal = producto.precio * cantidad
            print(f"{producto.nombre} x{cantidad} - Subtotal: ${subtotal:.2f}")
            total += subtotal
        print(f"Total: ${total:.2f}")
        return total

    def finalizar_compra(self):
        print("\n=== Recibo ===")
        total = self.mostrar_carrito()
        print("=================")
        print(f"Total a pagar: ${total:.2f}")
        print("Gracias por su compra.")
        self.carrito.clear()


# Ejemplo de uso
if __name__ == "__main__":
    pos = PuntoDeVenta()

    # Agregar productos al sistema
    pos.agregar_producto("001", "Manzana", 0.5)
    pos.agregar_producto("002", "Pan", 1.0)
    pos.agregar_producto("003", "Leche", 1.5)

    while True:
        print("\n=== Menú ===")
        print("1. Ver productos")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pos.mostrar_productos()
        elif opcion == "2":
            codigo = input("Ingrese el código del producto: ")
            cantidad = int(input("Ingrese la cantidad: "))
            pos.agregar_al_carrito(codigo, cantidad)
        elif opcion == "3":
            pos.mostrar_carrito()
        elif opcion == "4":
            pos.finalizar_compra()
        elif opcion == "5":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida.")
