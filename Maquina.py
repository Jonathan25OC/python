import pygame
import sys

# Inicializar constantes
CELL_SIZE = 40   # Tamaño de cada celda de la cinta
FONT_SIZE = 30
TAPE_LENGTH = 10  # Longitud inicial de la cinta visible

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Definición de la máquina de Turing
class TuringMachine:
    def __init__(self, tape, blank_symbol=' '):
        self.tape = list(tape) + [blank_symbol] * (TAPE_LENGTH - len(tape))  # Cinta con espacio en blanco
        self.head_position = 0  # Posición inicial del cabezal
        self.blank_symbol = blank_symbol  # Símbolo en blanco
        self.state = 'q0'  # Estado inicial

    def step(self, transitions):
        symbol = self.tape[self.head_position]
        if (self.state, symbol) in transitions:
            new_state, write_symbol, direction = transitions[(self.state, symbol)]
            self.tape[self.head_position] = write_symbol
            # Mover el cabezal
            if direction == 'R':
                self.head_position += 1
                if self.head_position >= len(self.tape):
                    self.tape.append(self.blank_symbol)  # Extiende la cinta a la derecha
            elif direction == 'L':
                self.head_position -= 1
                if self.head_position < 0:
                    self.tape.insert(0, self.blank_symbol)  # Extiende la cinta a la izquierda
                    self.head_position = 0
            self.state = new_state

    def get_tape(self):
        return ''.join(self.tape)

# Configuración de las transiciones
transitions = {
    ('q0', '0'): ('q0', '0', 'R'),  # Si es 0, permanece en q0 y mueve a la derecha
    ('q0', '1'): ('q0', '0', 'R'),  # Si es 1, cambia a 0 y mueve a la derecha
    ('q0', ' '): ('qf', ' ', 'R')   # Si encuentra espacio en blanco, va a estado final
}

# Inicialización de pygame
pygame.init()
screen = pygame.display.set_mode((CELL_SIZE * TAPE_LENGTH, 100))
pygame.display.set_caption("Máquina de Turing")
font = pygame.font.Font(None, FONT_SIZE)

# Función para dibujar la cinta y el cabezal
def draw_tape(machine):
    screen.fill(WHITE)
    for i, symbol in enumerate(machine.tape[:TAPE_LENGTH]):
        x = i * CELL_SIZE
        color = BLUE if i == machine.head_position else BLACK
        pygame.draw.rect(screen, color, (x, 20, CELL_SIZE, CELL_SIZE), 2)
        text = font.render(symbol, True, color)
        screen.blit(text, (x + 10, 30))

    state_text = font.render(f"Estado: {machine.state}", True, BLACK)
    screen.blit(state_text, (10, 70))
    pygame.display.flip()

# Cinta inicial y creación de la máquina de Turing
initial_tape = ['0', '0', '1', '0', '1', '1', '1', '0', '1']
machine = TuringMachine(initial_tape)

# Bucle principal de la animación
clock = pygame.time.Clock()
running = True
while running:
    draw_tape(machine)
    pygame.time.delay(500)  # Retardo entre pasos (ajusta según lo necesites)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Realizar un paso de la máquina de Turing
    if machine.state != 'qf':  # Continuar hasta el estado final
        machine.step(transitions)
    else:
        running = False  # Detener si alcanza el estado final

    clock.tick(1)  # Velocidad de actualización de la animación

pygame.quit()
sys.exit()
