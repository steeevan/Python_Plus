import pygame
from settings import *

class Paddle:
    def __init__(self, x, y, is_ai=False):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.velocity = 0
        self.acceleration = 0.5
        self.max_speed = 6
        self.damping = 0.9
        self.is_ai = is_ai

    def move(self, up, down):
        if up:
            self.velocity -= self.acceleration
        elif down:
            self.velocity += self.acceleration
        else:
            self.velocity *= self.damping

        self.velocity = max(-self.max_speed, min(self.velocity, self.max_speed))
        self.rect.y += self.velocity

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity = 0

    def move_toward(self, target_y):
        center = self.rect.centery
        if center < target_y:
            self.velocity += self.acceleration
        elif center > target_y:
            self.velocity -= self.acceleration
        else:
            self.velocity *= self.damping

        self.velocity = max(-self.max_speed, min(self.velocity, self.max_speed))
        self.rect.y += self.velocity

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.velocity = 0

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE if self.is_ai else RED, self.rect)
