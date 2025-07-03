import time
import pygame

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, target):
        print(f"{self.name} attacks! BANG")
        target.take_damage(10)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took damage! OUCH")
        print(f"{self.name} has {self.health} hearts.")

class Player(Character):
    def __init__(self, name, color):
        super().__init__(name)
        self.x = 100
        self.y = 300
        self.color = color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))

class Enemy(Character):
    pass



# asking use for player color and name
print(" ")
player_name = input("Input your players name: ") # asking for player name
player_color = (255,255,255)

player1 = Player(player_name, player_color)
enemy = Enemy("Gargamor")
time.sleep(3)
print(" ")

# player 1 attacks first
player1.attack(enemy)

# wait 5 seconds
time.sleep(5)
print(" ")

# enemy attacks two times
enemy.attack(player1)
print(" ")
time.sleep(1)
enemy.attack(player1)

# CREATING THE GUI
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

# CONTROLLING THE GUI
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # move left and right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player1.move(10, 0)
        if keys[pygame.K_LEFT]:
            player1.move(-10,0)
        #move up and down
        if keys[pygame.K_UP]:
            player1.move(0,-10)
        if keys[pygame.K_DOWN]:
            player1.move(0,10)

    screen.fill((0,0,0))
    player1.draw(screen)
    pygame.display.flip()
    clock.tick(60)

    


    