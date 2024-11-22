class MaquinaDeTuring:
    def __init__(self, cinta, estado_inicial, estado_final, transiciones):
        self.cinta = list(cinta)
        self.posicion_cabezal = 0
        self.estado_actual = estado_inicial
        self.estado_final = estado_final
        self.transiciones = transiciones

    def ejecutar(self):
        while self.estado_actual != self.estado_final:
            simbolo_actual = self.cinta[self.posicion_cabezal]
            accion = self.transiciones.get((self.estado_actual, simbolo_actual))

            if accion is None:
                print("Transición no definida. La máquina se detuvo.")
                break

            nuevo_estado, nuevo_simbolo, movimiento = accion
            self.cinta[self.posicion_cabezal] = nuevo_simbolo
            self.estado_actual = nuevo_estado

            if movimiento == "R":
                self.posicion_cabezal += 1
                if self.posicion_cabezal == len(self.cinta):
                    self.cinta.append(" ")
            elif movimiento == "L":
                self.posicion_cabezal -= 1
                if self.posicion_cabezal < 0:
                    self.cinta.insert(0, " ")
                    self.posicion_cabezal = 0

    def mostrar_cinta(self):
        print("Cinta:", "".join(self.cinta).strip())
        print("Posición del cabezal:", self.posicion_cabezal)
        print("Estado actual:", self.estado_actual)


# Definimos la cinta inicial con dos números binarios separados por un "_"
cinta_inicial = "101_11"

# Transiciones para la suma binaria
transiciones = {
    # Escanea el primer número y encuentra el separador
    ("q0", "1"): ("q0", "1", "R"),
    ("q0", "0"): ("q0", "0", "R"),
    ("q0", "_"): ("q1", "_", "R"),  # Encuentra el separador y avanza al segundo número

    # Procesa el segundo número
    ("q1", "1"): ("q1", "1", "R"),
    ("q1", "0"): ("q1", "0", "R"),
    ("q1", " "): ("q2", " ", "L"),  # Llega al final del segundo número y retrocede

    # Realiza la suma bit a bit
    ("q2", "1"): ("q3", "0", "L"),  # Lleva el acarreo
    ("q2", "0"): ("q4", "1", "L"),  # No lleva acarreo
    ("q2", "_"): ("qf", " ", "R"),  # Finaliza

    # Gestión del acarreo
    ("q3", "1"): ("q3", "0", "L"),
    ("q3", "0"): ("q4", "1", "L"),
    ("q3", "_"): ("qf", "1", "R"),  # Si hay acarreo al final, escribe 1 y finaliza
}

# Crear y ejecutar la máquina
maquina = MaquinaDeTuring(cinta_inicial, "q0", "qf", transiciones)
print("Antes de ejecutar:")
maquina.mostrar_cinta()
maquina.ejecutar()
print("\nDespués de ejecutar:")
maquina.mostrar_cinta()
