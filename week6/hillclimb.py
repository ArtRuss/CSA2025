import pygame
import sys
from car import Car

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hill Climb")

# Set up the clock
clock = pygame.time.Clock()
FPS = 60  # frames per second

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

car = Car()
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        car.gas()
    elif keys[pygame.K_LEFT]:
        car.brake()
    elif keys[pygame.K_DOWN]:
        pass
    else:
        car.coast()

    car.gravity()

    # collisions:
    if car.y + car.H >= 500:
        car.vy *= -0.9


    car.move()
    # Draw everything
    screen.fill(BLUE)  # Clear screen
    print(car.x, car.y)
    pygame.draw.rect(screen, RED, pygame.Rect(car.x, car.y, car.W, car.H))

    pygame.display.flip()  # Update the screen

    clock.tick(FPS)  # Cap the frame rate

pygame.quit()
sys.exit()
