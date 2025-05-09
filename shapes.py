import pygame
from typing import Tuple
import formulas

class Circle:
    def __init__(self, radius: int, position: Tuple, color: Tuple):
        self.radius = radius
        self.position = position
        self.color = color

    def draw(self, screen):
        self.circle = pygame.draw.circle(screen, self.color, self.position, self.radius)

    def fall(self):
        self.circle.y += formulas.distance_travelled(formulas.calculate_velocity(formulas.gravity, 1), 1)