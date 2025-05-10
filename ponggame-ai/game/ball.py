import pygame
import random
from settings import *

class Ball:
    def __init__(self):
        self.radius = BALL_RADIUS
        self.reset()
        self.trail = []
        self.slow_motion = False
        self.slow_timer = 0

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.dx = random.choice([-4, 4])
        self.dy = random.choice([-4, 4])
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.trail = []
        self.slow_motion = True
        self.slow_timer = 60  # 1 second of slow-motion at 60 FPS

    def update(self):
        speed_factor = 0.5 if self.slow_motion and self.slow_timer > 0 else 1.0

        self.x += self.dx * speed_factor
        self.y += self.dy * speed_factor

        if self.y <= 0 or self.y >= HEIGHT:
            self.dy *= -1

        self.rect.x = self.x
        self.rect.y = self.y

        self.trail.append((int(self.x), int(self.y)))
        if len(self.trail) > 12:
            self.trail.pop(0)

        if self.slow_motion:
            self.slow_timer -= 1
            if self.slow_timer <= 0:
                self.slow_motion = False

        # Gradual speed increase
        if abs(self.dx) < MAX_BALL_SPEED:
            self.dx += BALL_SPEED_INCREMENT * (1 if self.dx > 0 else -1)
        if abs(self.dy) < MAX_BALL_SPEED:
            self.dy += BALL_SPEED_INCREMENT * (1 if self.dy > 0 else -1)

    def check_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            offset = (self.y - paddle.rect.centery) / (PADDLE_HEIGHT // 2)
            bounce_angle = offset * 5
            self.dx *= -1
            self.dy += bounce_angle

            # Trigger screen shake event
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {"shake": True}))

    def draw(self, screen):
        for i, (tx, ty) in enumerate(self.trail):
            radius = max(1, self.radius - i // 2)
            color = (200, 200, 200)
            pygame.draw.circle(screen, color, (tx, ty), radius)

        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)
