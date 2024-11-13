import pygame
import random

# Inicializamos pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configuramos la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego Simple")

# Clase para el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

# Clase para el obstáculo
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(50, SCREEN_HEIGHT // 2)
        self.speed_x = 5

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed_x *= -1  # Cambia de dirección al chocar con los bordes

# Inicializamos jugador y obstáculo
player = Player()
obstacle = Obstacle()

# Grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(obstacle)

# Control de FPS
clock = pygame.time.Clock()
running = True

# Bucle principal del juego
while running:
    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar estado de los sprites
    all_sprites.update()

    # Comprobar colisiones
    if pygame.sprite.collide_rect(player, obstacle):
        print("¡Juego terminado!")
        running = False

    # Dibujar en pantalla
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(30)

# Salir del juego
pygame.quit()
