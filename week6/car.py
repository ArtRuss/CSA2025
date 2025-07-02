import math

class Car:
    def __init__(self):
        self.max_speed = 10
        self.W = 100
        self.H = 50
        self.x = 400
        self.y = 300
        self.vx = 0
        self.vy= 0
        self.ax = 0
        self.ay = 0.5 # (positive y is down)

    def gas(self):
        self.ax = 1
        self.vx += self.ax
        if self.vx > self.max_speed:
            self.vx = self.max_speed

    def brake(self):
        self.ax = -1
        self.vx += self.ax
        if self.vx < -self.max_speed:
            self.vx = -self.max_speed

    def coast(self):
        self.vx *= 0.95

    def gravity(self):
        self.vy += self.ay

    def move(self):
        self.x += self.vx
        self.y += self.vy
