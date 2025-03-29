import pygame

class Ball:
    def __init__(self, x, y, radius, speed):
        self.rect = pygame.Rect(x,y,radius, radius)
        self.speed_x = speed
        self.speed_y = speed
        self.radius = radius

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= 480:
            self.speed_y *= -1
    
    def reset(self, x, y ):
        self.rect.x = x
        self.rect.y = y
        self.speed_x *= -1
        self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255,255,255), self.rect)

