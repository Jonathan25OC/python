class MaquinaDeTuring:
    def __init__(self, cinta, estado_inicial, estado_final, transiciones):
        self.cinta = list(cinta)  # Convertimos la cinta en una lista para modificarla
        self.posicion_cabezal = 0  # Posición inicial del cabezal
        self.estado_actual = estado_inicial  # Estado inicial
        self.estado_final = estado_final  # Estado final
        self.transiciones = transiciones  # Tabla de transiciones

    def ejecutar(self):
        while self.estado_actual != self.estado_final:
            simbolo_actual = self.cinta[self.posicion_cabezal]
            accion = self.transiciones.get((self.estado_actual, simbolo_actual))

            if accion is None:
                print("La máquina se detuvo debido a una transición no definida.")
                break

            nuevo_estado, nuevo_simbolo, movimiento = accion
            self.cinta[self.posicion_cabezal] = nuevo_simbolo
            self.estado_actual = nuevo_estado

            if movimiento == "R":  # Mover a la derecha
                self.posicion_cabezal += 1
                if self.posicion_cabezal == len(self.cinta):
                    self.cinta.append(" ")  # Extender la cinta con un espacio en blanco
            elif movimiento == "L":  # Mover a la izquierda
                self.posicion_cabezal -= 1
                if self.posicion_cabezal < 0:
                    self.cinta.insert(0, " ")  # Extender la cinta a la izquierda con un espacio en blanco
                    self.posicion_cabezal = 0

    def mostrar_cinta(self):
        print("Cinta:", "".join(self.cinta))
        print("Posición del cabezal:", self.posicion_cabezal)
        print("Estado actual:", self.estado_actual)


# Definimos una cinta inicial
cinta_inicial = "1011"

# Definimos las transiciones: (estado_actual, simbolo_actual) -> (nuevo_estado, nuevo_simbolo, movimiento)
transiciones = {
    ("q0", "1"): ("q0", "1", "R"),
    ("q0", "0"): ("q0", "0", "R"),
    ("q0", " "): ("q1", " ", "L"),  # Cuando llega al final, pasa al estado q1
    ("q1", "1"): ("q1", "0", "L"),  # Invierte un 1 a 0 en estado q1
    ("q1", "0"): ("q1", "1", "L"),  # Invierte un 0 a 1 en estado q1
    ("q1", " "): ("qf", " ", "R"),  # Finaliza en qf
}

# Crear y ejecutar la máquina de Turing
maquina = MaquinaDeTuring(cinta_inicial, "q0", "qf", transiciones)
maquina.mostrar_cinta()
maquina.ejecutar()
maquina.mostrar_cinta()
