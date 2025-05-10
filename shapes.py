import pygame
from typing import Tuple
import formulas

class Circle:
    def __init__(self, color: Tuple, x_pos: int, y_pos:int , radius: int):
        self.radius = radius
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.velocity = 0

    def render(self, screen):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def draw(self, screen, newposition):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, newposition), self.radius)

    def fall(self, time):
        self.velocity += formulas.calculate_velocity(time)
        self.y_pos += formulas.distance_travelled(self.velocity, time)