import pygame

class Enemy:
    def __init__(self,path):
        self.x,self.y = path[0]
        self.path = path
        self.speed = 2
        self.health = 50
        self.image = pygame.image.load("assets/images/enemy.png")
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.current_path_index = 0

    def update(self):
        if self.current_path_index < len(self.path - 1):
            target_x, target_y = self.path(self.current_path_index + 1)
            dx, dy = target_x - self.x, target_y - self.y
            distance = (dx**2 + dy**2)**0.5

            if distance <= self.speed:
                self.x, self.y = target_x, target_y
                self.current_path_index += 1
        self.rect.center = (self.x,self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def take_damage(self,damage):
        self.health -= damage
        if self.health <= 0:
            return True
        return False
    