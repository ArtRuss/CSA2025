import time

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
    pass

class Enemy(Character):
    pass

# creating the character objects
print(" ")
player_name = input("Input your players name: ") # asking for player name
player1 = Player(player_name)
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


    