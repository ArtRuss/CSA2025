import pygame

class Car:
    def __init__(self, speed, x, y):
        self.image = pygame.image.load("car.png")
        self.image = pygame.transform.scale(self.image, (145, 92))
        self.speed = speed
        self.x = x
        self.y = y

    def accelerate(self):
        self.speed += 0.5
        # Ensure speed does not exceed a maximum value
        if self.speed > 15:
            self.speed = 15

    def brake(self):
        self.speed -= 0.5
        # Ensure speed does not exceed a maximum value
        if self.speed < -15:
            self.speed = -15
    
    def draw_car(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def update_pos(self):
        self.x += self.speed
        # Make sure the car doesn't go off-screen
        if self.x > 800 - self.image.get_width():
            self.x = 800 - self.image.get_width()
            self.speed = 0
        elif self.x < 0:
            self.x = 0
            self.speed = 0

class Character:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Level:
    def __init__(self, name, difficulty, length):
        self.name = name
        self.difficulty = difficulty
        self.length = length
    
class Coin:
    def __init__(self, x_coordinate, y_coordinate, value):
        self.x = x_coordinate
        self.y = y_coordinate
        self.value = value

if __name__ == "__main__":
    car = Car(0, 10, 20)
    
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hill Climb Racing")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            car.accelerate()
        if keys[pygame.K_DOWN]:
            car.brake()
        car.update_pos()
        car.draw_car(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))  # Clear the screen
        clock.tick(60)  # Use clock to control frame rate

    pygame.quit()