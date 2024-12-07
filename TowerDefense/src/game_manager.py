import pygame
from src.tower import Tower
from src.enemy import Enemy

class GameManager:
    def __init__(self, money, lives):
        self.money = money
        self.lives = lives
        self.towers = [Tower(100, 200)]  # Add a test tower at position (100, 200)
        self.enemies = [Enemy([(50, 300), (200, 300), (400, 300), (600, 300), (750, 300)])]  # Add a test enemy
        self.path = [(50, 300), (200, 300), (400, 300), (600, 300), (750, 300)]
    def update(self):
        for enemy in self.enemies[:]:
            enemy.update()
            if enemy.health <= 0:
                self.enemies.remove(enemy)

        for tower in self.towers:
            tower.attack(self.enemies)
    
    def add_enemy(self):
        self.enemies.append(Enemy(self.path))

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for tower in self.towers:
            tower.draw(screen)

    def add_tower(self,x,y):
        if self.money >= 100: # tower cost
            self.tower.append(Tower(x,y))
            self.money -= 100
    