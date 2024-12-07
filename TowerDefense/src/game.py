import pygame
from src.settings import SCREEN_HEIGHT,SCREEN_WIDTH,FPS,INITIAL_LIVES,INITIAL_MONEY
from src.tower import Tower
from src.enemy import Enemy
from src.game_manager import GameManager

class TowerDefenseGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption("Tower Defense Game")
        self.clock = pygame.time.Clock()
        self.running = True

        # game states
        self.money = INITIAL_MONEY
        self.lives = INITIAL_LIVES
        self.game_manager = GameManager(self.money,self.lives)
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        self.game_manager.update()
    def draw(self):
        self.screen.fill((30,30,30)) # black background
        self.game_manager.draw(self.screen)
        pygame.display.flip()
