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
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Configuración de pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Captura las estrellas")

# Clase del jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
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

# Clase de la estrella
class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

# Inicializamos el jugador y la estrella
player = Player()
star = Star()

# Grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(star)

# Variables de puntuación y tiempo
score = 0
time_left = 30  # Tiempo en segundos

# Reloj para controlar el tiempo
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()  # Tiempo inicial

# Bucle principal del juego
running = True
while running:
    # Calcular tiempo restante
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    if seconds > time_left:
        print("Tiempo agotado. ¡Juego terminado!")
        running = False

    # Procesar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar estado de los sprites
    all_sprites.update()

    # Comprobar colisión entre el jugador y la estrella
    if pygame.sprite.collide_rect(player, star):
        score += 1  # Aumenta la puntuación
        print("¡Puntuación:", score)
        star.rect.x = random.randint(0, SCREEN_WIDTH - star.rect.width)  # Cambia la posición de la estrella
        star.rect.y = random.randint(0, SCREEN_HEIGHT - star.rect.height)

    # Dibujar en pantalla
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Mostrar puntuación y tiempo en pantalla
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Puntuación: {score}", True, BLACK)
    time_text = font.render(f"Tiempo restante: {time_left - seconds}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 50))

    pygame.display.flip()

    # Control de FPS
    clock.tick(30)

# Salir del juego
pygame.quit()
