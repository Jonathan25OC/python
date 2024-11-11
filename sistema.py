class Venta:
    def __init__(self, producto, cantidad, precio_unitario):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def total_venta(self):
        return self.cantidad * self.precio_unitario

class SistemaVentas:
    def __init__(self):
        self.ventas = []
        self.costos = 0
        self.ingresos = 0

    def agregar_venta(self, venta):
        self.ventas.append(venta)
        self.ingresos += venta.total_venta()

    def agregar_costo(self, costo):
        self.costos += costo

    def generar_estado_resultado(self):
        utilidad_bruta = self.ingresos - self.costos
        print("Estado de Resultados")
        print("Ingresos: $", self.ingresos)
        print("Costos: $", self.costos)
        print("Utilidad Bruta: $", utilidad_bruta)

# Ejemplo de uso
sistema = SistemaVentas()

# Agregar ventas
venta1 = Venta("Producto A", 10, 50)  # 10 unidades a $50 cada una
venta2 = Venta("Producto B", 5, 100)  # 5 unidades a $100 cada una
sistema.agregar_venta(venta1)
sistema.agregar_venta(venta2)

# Agregar costos
sistema.agregar_costo(200)  # Costo fijo de $200

# Generar estado de resultados
sistema.generar_estado_resultado()

