class MaquinaBorraCintas:
    def __init__(self, cinta):
        self.cinta = list(cinta)  # La cinta se convierte en una lista para facilitar las operaciones
        self.cabezal = 0  # Posición inicial del cabezal
        self.terminado = False  # Estado de finalización

    def mover_cabezal(self, direccion):
        if direccion == 'D':
            self.cabezal += 1
        elif direccion == 'I':
            self.cabezal -= 1

        # Expandir la cinta con espacios en blanco si el cabezal se sale de los límites actuales
        if self.cabezal < 0:
            self.cabezal = 0
            self.cinta.insert(0, ' ')
        elif self.cabezal >= len(self.cinta):
            self.cinta.append(' ')

    def borrar(self):
        # Borrar el símbolo actual en la posición del cabezal
        self.cinta[self.cabezal] = ' '

    def escribir(self, simbolo):
        # Escribir un símbolo en la posición actual del cabezal
        self.cinta[self.cabezal] = simbolo

    def procesar(self):
        # Lógica para recorrer la cinta
        while not self.terminado:
            simbolo_actual = self.cinta[self.cabezal]
            
            if simbolo_actual == '1':
                self.borrar()  # Borra el símbolo si es '1'
                self.mover_cabezal('D')  # Se mueve a la derecha
            elif simbolo_actual == '0':
                self.escribir('1')  # Escribe un '1' en lugar de '0'
                self.mover_cabezal('I')  # Se mueve a la izquierda
            else:
                # Si el símbolo es un espacio en blanco, detiene la máquina
                self.terminado = True

            # Muestra el estado actual de la cinta y la posición del cabezal
            print("".join(self.cinta), f"(Cabezal: {self.cabezal})")


# Ejemplo de uso de la máquina
cinta_inicial = "11001"  # Cinta inicial con algunos símbolos
maquina = MaquinaBorraCintas(cinta_inicial)
maquina.procesar()
