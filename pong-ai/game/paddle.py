import pygame

class Paddle:
    def __init__(self,x,y,width,height,speed):
        self.rect = pygame.Rect(x,y,width,height)
        self.speed = speed
    

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        
        self.rect.y = max(min(self.rect.y, 480 - self.rect.height),0)

    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),self.rect)
