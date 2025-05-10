import pygame
from settings import *

class Score:
    def __init__(self):
        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", FONT_SIZE)

    def draw(self, screen):
        player_text = self.font.render(f"Player: {self.player_score}", True, WHITE)
        ai_text = self.font.render(f"AI: {self.ai_score}", True, WHITE)
        screen.blit(player_text, (WIDTH // 4, 20))
        screen.blit(ai_text, (WIDTH * 3 // 4 - ai_text.get_width(), 20))
