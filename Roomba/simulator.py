import pygame
from room import Room
from vacuum import Vacuum

class Simulator:
    def __init__(self, rows=10, cols=10, cell_size=50):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.width = cols * cell_size
        self.height = rows * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Smart Vacuum Cleaner AI - A* Version")
        self.clock = pygame.time.Clock()
        self.room = Room(rows, cols)
        self.vacuum = Vacuum(self.room)

    def draw(self):
        self.screen.fill((255, 255, 255))
        for row in range(self.rows):
            for col in range(self.cols):
                color = (200, 200, 200) if self.room.grid[row][col] == 1 else (255, 255, 255)
                pygame.draw.rect(self.screen, color, (col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.rect(self.screen, (0, 0, 0), (col*self.cell_size, row*self.cell_size, self.cell_size, self.cell_size), 1)
        pygame.draw.circle(self.screen, (0, 0, 255), 
                           (self.vacuum.col*self.cell_size + self.cell_size//2, self.vacuum.row*self.cell_size + self.cell_size//2), 
                           self.cell_size//3)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.clock.tick(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.vacuum.clean()
            self.vacuum.move()
            self.draw()
            if self.room.all_clean():
                print("✅ All clean!")
                running = False
