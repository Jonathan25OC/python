class MaquinaBorraCintas:
    def __init__(self, cinta, estado_inicial):
        self.cinta = list(cinta)  # Convertimos la cinta a una lista de caracteres
        self.cabezal = 0  # Posición inicial del cabezal
        self.estado = estado_inicial  # Estado inicial de la máquina
        self.terminado = False

    def mover_cabezal(self, direccion):
        if direccion == 'D':
            self.cabezal += 1
        elif direccion == 'I':
            self.cabezal -= 1

        # Asegurarnos de que el cabezal esté dentro de los límites de la cinta
        if self.cabezal < 0:
            self.cabezal = 0
            self.cinta.insert(0, ' ')
        elif self.cabezal >= len(self.cinta):
            self.cinta.append(' ')

    def borrar(self):
        # Borrar el símbolo actual en la posición del cabezal
        self.cinta[self.cabezal] = ' '

    def escribir(self, simbolo):
        self.cinta[self.cabezal] = simbolo

    def procesar(self):
        # Ejemplo simple de procesamiento de una cinta
        while not self.terminado:
            simbolo_actual = self.cinta[self.cabezal]
            
            if simbolo_actual == '1':
                self.borrar()
                self.mover_cabezal('D')
            elif simbolo_actual == '0':
                self.escribir('1')
                self.mover_cabezal('I')
            else:
                # Si encontramos un símbolo en blanco, terminamos el proceso
                self.terminado = True

            # Mostrar el estado actual de la cinta
            print("".join(self.cinta), f"(Cabezal: {self.cabezal})")


# Ejemplo de uso
cinta_inicial = "11001"  # Cinta inicial con algunos símbolos
maquina = MaquinaBorraCintas(cinta_inicial, estado_inicial="q0")
maquina.procesar()
