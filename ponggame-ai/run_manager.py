import pygame
from settings import *

class RunManager:
    def __init__(self):
        self.run_count = 1
        self.font = pygame.font.SysFont("Arial", FONT_SIZE)

    def increment(self):
        self.run_count += 1

    def draw(self, screen):
        text = self.font.render(f"Run: {self.run_count}", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))
