import pygame
import sys
import math
import random

pygame.init()

# screen settings
WIDTH, HEIGHT, = 800, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Tower Defense with Two Tower Types")

# setup screen frame rates
FPS = 60
GRID_SIZE = 40
ROWS = HEIGHT // GRID_SIZE
COLS = HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139,69,19)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
DARKGREEN = (0, 155, 0)
FLASH_COLOR = (255, 0, 0, 100)  # semi-transparent red

# FOnts
FONT = pygame.font.SysFont("arial", 20)

# game parameterss
STARTING_HEALTH = 20
STARTING_SCORE = 0
STARTING_MONEY = 200

# TOWER PROPERTIES
# TWO TOWER TYPES fAST OR SLOW
FAST_TOWER_COST = 50
FAST_TOWER_DAMAGE = 1
FAST_TOWER_FIRE_RATE = 30
SLOW_TOWER_COST = 100
SLOW_TOWER_DAMAGE = 4
SLOW_TOWER_FIRE_RATE = 90

TOWER_RANGE = 150

# ENEMY SETTINGS   
ENEMY_SPEED = 1.0
ENEMY_SIZE = 20
ENEMY_HEALTH = 10

# BULLET SETTINGS
BULLET_SPEED = 5
BULLET_SIZE = 4

# DEFINE THE BASE LOCATION (END POINT FOR ALL PATHS)
BASE_X,BASE_Y = WIDTH - GRID_SIZE*2, HEIGHT // 2
# Define paths as lists of (x,y) pixel coordianates (waypoints)
PATH_TOP = [
    (0,HEIGHT//4),
    (WIDTH//3, HEIGHT//4),
    (2*WIDTH//3,HEIGHT//3),
    (BASE_X,BASE_Y)
]
PATH_MID = [
    (0, HEIGHT//2),
    (WIDTH//3, HEIGHT//2),
    (2*WIDTH//3, HEIGHT//2),
    (BASE_X, BASE_Y)
]

PATH_BOT = [
    (0, 3*HEIGHT//4),
    (WIDTH//3, 3*HEIGHT//4),
    (2*WIDTH//3, HEIGHT//2),
    (BASE_X, BASE_Y)
]

ALL_PATHS = [PATH_TOP,PATH_MID,PATH_BOT]

def path_cells_for_path(path):
    cells = set()
    for i in range(len(path) - 1):
        x1,y1 = path[i]
        x2,y2 = path[i+1]
        dist = math.hypot(x2 - x1, y2 - y1)
        steps = int( dist // (GRID_SIZE/2))
        for s in range(steps + 1):
            x = x1 + (x2 - x1)*s/steps
            y = y1 + (y2 - y1)*s/steps
            gx = int(x // GRID_SIZE)
            gy = int(y // GRID_SIZE)
            cells.add((gx,gy))
    return cells

ALL_PATH_CELLS = set()
for p in ALL_PATHS:
    ALL_PATH_CELLS |= path_cells_for_path(p)

class Enemy:
    def __init__(self,path):
        self.path = path
        self.health = ENEMY_HEALTH
        self.max_health = ENEMY_HEALTH
        self.current_waypoint = 0
        self.x, self.y = self.path[0]
    
    def update(self):
        # move along the path
        if self.current_waypoint < len(self.path) - 1:
            tx,ty = self.path[self.current_waypoint+1]
            dx = tx - self.x
            dy = ty - self.y
            dist = math.sqrt(dx*dx + dy*dy)
            if dist != 0:
                dx /= dist
                dy /= dist
            self.x += dx * ENEMY_SPEED
            self.y += dy * ENEMY_SPEED

            # check if reached the next waypoint
            if math.hypot(tx - self.x, ty - self.y) < ENEMY_SPEED:
                self.x, self.y = tx,ty
                self.current_waypoint += 1

    def reached_end(self):
        return self.current_waypoint == len(self.path)-1 and (self.x,self.y) == self.path[-1]

    def draw(self,surf):
        # draw enemy
        rect = pygame.Rect(self.x - ENEMY_SIZE//2, self.y - ENEMY_SIZE//2, ENEMY_SIZE,ENEMY_SIZE)
        pygame.draw.rect(surf, RED, rect)

        # draw health bar
        bar_width = ENEMY_SIZE
        health_radio = self.health / self.max_health
        health_bar_width = int(bar_width * health_radio)
        bar_rect = pygame.Rect(self.x - ENEMY_SIZE//2, self.y - ENEMY_SIZE//2 - 8, bar_width,5)
        pygame.draw.rect(surf,BLACK,bar_rect) # outline of healthbar
        inner_rect = pygame.Rect(self.x - ENEMY_SIZE//2, self.y - ENEMY_SIZE//2 - 8, health_bar_width,5)
        pygame.draw.rect(surf,GREEN,inner_rect)

    def is_alive(self):
        return self.health > 0
    def get_rect(self):
        return pygame.Rect(self.x - ENEMY_SIZE//2, self.y - ENEMY_SIZE//2, ENEMY_SIZE,ENEMY_SIZE)
    
    