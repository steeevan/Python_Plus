import pygame

class Tower:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.range = 100
        self.damage = 10
        self.image = pygame.image.load("assets/images/tower.png")
        self.rect = self.image.get_rect(center=(self.x,self.y))

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def attack(self,enemies):
        for enemy in enemies:
            if self.in_range(enemy):
                enemy.take_damage(self.damage)
    
    def in_range(self,enemy):
        distance = ((self.x - enemy.x)**2 + (self.y - enemy.y)**2)**0.5
        return distance <= self.range
    