import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 400

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boundary Detection")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Sprite properties
sprite_color = WHITE
sprite_size = 30
sprite_x, sprite_y = WIDTH // 2, HEIGHT // 2  # Start at the center
sprite_speed = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Update sprite position
    if keys[pygame.K_UP]:
        sprite_y -= sprite_speed
    if keys[pygame.K_DOWN]:
        sprite_y += sprite_speed
    if keys[pygame.K_LEFT]:
        sprite_x -= sprite_speed
    if keys[pygame.K_RIGHT]:
        sprite_x += sprite_speed

    # Check for boundary collision
    if sprite_x <= 0 or sprite_x + sprite_size >= WIDTH or sprite_y <= 0 or sprite_y + sprite_size >= HEIGHT:
        sprite_color = random_color()

    # Prevent the sprite from going out of bounds
    sprite_x = max(0, min(WIDTH - sprite_size, sprite_x))
    sprite_y = max(0, min(HEIGHT - sprite_size, sprite_y))

    # Clear screen
    screen.fill(BLACK)

    # Draw sprite
    pygame.draw.rect(screen, sprite_color, (sprite_x, sprite_y, sprite_size, sprite_size))

    # Update display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
