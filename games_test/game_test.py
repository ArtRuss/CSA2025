import pygame

# initialize pygame
pygame.init()

# create a window (makes the window you see)
screen = pygame.display.set_mode((800, 600))

# create a clock (helps you control how fast your game loop runs)
clock = pygame.time.Clock()

# variables for positions
player_x = 100
player_y = 300

# make your main loop (runs forever until you quit the game)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_x += 5
            if event.key == pygame.K_LEFT:
                player_x -= 5
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,255,0), (player_x,player_y,50,50))
    pygame.display.flip()
    clock.tick(60)
