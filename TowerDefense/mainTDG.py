import pygame
import sys
import math
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense with Two Tower Types")

FPS = 60
GRID_SIZE = 40
ROWS = HEIGHT // GRID_SIZE
COLS = WIDTH // GRID_SIZE

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

# Fonts
FONT = pygame.font.SysFont("arial", 20)

# Game parameters
STARTING_HEALTH = 20
STARTING_SCORE = 0
STARTING_MONEY = 200

# Tower properties
# Two tower types: Fast and Slow
FAST_TOWER_COST = 50
FAST_TOWER_DAMAGE = 1
FAST_TOWER_FIRE_RATE = 30  # Faster firing
SLOW_TOWER_COST = 100
SLOW_TOWER_DAMAGE = 4
SLOW_TOWER_FIRE_RATE = 90  # Slower firing

TOWER_RANGE = 150

# Enemy settings
ENEMY_SPEED = 1.0
ENEMY_SIZE = 20
ENEMY_HEALTH = 10

# Bullet settings
BULLET_SPEED = 5
BULLET_SIZE = 4

# Define the base location (the end point for all paths)
BASE_X, BASE_Y = WIDTH - GRID_SIZE*2, HEIGHT // 2

# Define paths as lists of (x,y) pixel coordinates (waypoints)
PATH_TOP = [
    (0, HEIGHT//4),
    (WIDTH//3, HEIGHT//4),
    (2*WIDTH//3, HEIGHT//3),
    (BASE_X, BASE_Y)
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

ALL_PATHS = [PATH_TOP, PATH_MID, PATH_BOT]

def path_cells_for_path(path):
    cells = set()
    for i in range(len(path)-1):
        x1, y1 = path[i]
        x2, y2 = path[i+1]
        dist = math.hypot(x2 - x1, y2 - y1)
        steps = int(dist // (GRID_SIZE/2))
        for s in range(steps+1):
            x = x1 + (x2 - x1)*s/steps
            y = y1 + (y2 - y1)*s/steps
            gx = int(x // GRID_SIZE)
            gy = int(y // GRID_SIZE)
            cells.add((gx, gy))
    return cells

ALL_PATH_CELLS = set()
for p in ALL_PATHS:
    ALL_PATH_CELLS |= path_cells_for_path(p)

class Enemy:
    def __init__(self, path):
        self.path = path
        self.health = ENEMY_HEALTH
        self.max_health = ENEMY_HEALTH
        self.current_waypoint = 0
        self.x, self.y = self.path[0]

    def update(self):
        # Move along the path
        if self.current_waypoint < len(self.path)-1:
            tx, ty = self.path[self.current_waypoint+1]
            dx = tx - self.x
            dy = ty - self.y
            dist = math.sqrt(dx*dx + dy*dy)
            if dist != 0:
                dx /= dist
                dy /= dist
            self.x += dx * ENEMY_SPEED
            self.y += dy * ENEMY_SPEED

            # Check if reached the next waypoint
            if math.hypot(tx - self.x, ty - self.y) < ENEMY_SPEED:
                self.x, self.y = tx, ty
                self.current_waypoint += 1

    def reached_end(self):
        return self.current_waypoint == len(self.path)-1 and (self.x, self.y) == self.path[-1]

    def draw(self, surf):
        # Draw enemy
        rect = pygame.Rect(self.x - ENEMY_SIZE//2, self.y - ENEMY_SIZE//2, ENEMY_SIZE, ENEMY_SIZE)
        pygame.draw.rect(surf, RED, rect)

        # Draw health bar
        bar_width = ENEMY_SIZE
        health_ratio = self.health / self.max_health
        health_bar_width = int(bar_width * health_ratio)
        bar_rect = pygame.Rect(self.x - ENEMY_SIZE//2, self.y - ENEMY_SIZE//2 - 8, bar_width, 5)
        pygame.draw.rect(surf, BLACK, bar_rect)  # outline
        inner_rect = pygame.Rect(self.x - ENEMY_SIZE//2, self.y - ENEMY_SIZE//2 - 8, health_bar_width, 5)
        pygame.draw.rect(surf, GREEN, inner_rect)

    def is_alive(self):
        return self.health > 0

    def get_rect(self):
        return pygame.Rect(self.x - ENEMY_SIZE//2, self.y - ENEMY_SIZE//2, ENEMY_SIZE, ENEMY_SIZE)


class Tower:
    def __init__(self, grid_x, grid_y, damage, fire_rate, cost):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.damage = damage
        self.fire_rate = fire_rate
        self.last_shot = 0
        self.cost = cost

    def draw(self, surf):
        # Draw tower
        pygame.draw.rect(surf, BLUE, (self.grid_x * GRID_SIZE, self.grid_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Draw range circle (outline)
        center = (self.grid_x * GRID_SIZE + GRID_SIZE//2, self.grid_y * GRID_SIZE + GRID_SIZE//2)
        pygame.draw.circle(surf, DARKGREEN, center, TOWER_RANGE, 1)

    def can_shoot(self, frame_count):
        return (frame_count - self.last_shot) > self.fire_rate

    def get_center(self):
        cx = self.grid_x * GRID_SIZE + GRID_SIZE//2
        cy = self.grid_y * GRID_SIZE + GRID_SIZE//2
        return cx, cy

    def get_target_in_range(self, enemies):
        cx, cy = self.get_center()
        target_enemy = None
        target_dist = None
        for enemy in enemies:
            if enemy.is_alive():
                dist = math.sqrt((enemy.x - cx)**2 + (enemy.y - cy)**2)
                if dist <= TOWER_RANGE:
                    if target_dist is None or dist < target_dist:
                        target_dist = dist
                        target_enemy = enemy
        return target_enemy

    def shoot(self, enemies, frame_count, bullets):
        target_enemy = self.get_target_in_range(enemies)
        if target_enemy:
            cx, cy = self.get_center()
            ex, ey = target_enemy.x, target_enemy.y
            dx = ex - cx
            dy = ey - cy
            dist = math.sqrt(dx*dx + dy*dy)
            if dist != 0:
                dx /= dist
                dy /= dist
            # Create a bullet
            bullets.append(Bullet(cx, cy, dx, dy, self.damage))
            self.last_shot = frame_count


class Bullet:
    def __init__(self, x, y, dx, dy, damage):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.damage = damage

    def update(self):
        self.x += self.dx * BULLET_SPEED
        self.y += self.dy * BULLET_SPEED

    def draw(self, surf):
        pygame.draw.circle(surf, YELLOW, (int(self.x), int(self.y)), BULLET_SIZE)

    def get_rect(self):
        return pygame.Rect(self.x - BULLET_SIZE, self.y - BULLET_SIZE, BULLET_SIZE*2, BULLET_SIZE*2)

    def off_screen(self):
        return self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT


def draw_grid(surf):
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c*GRID_SIZE, r*GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if (c, r) in ALL_PATH_CELLS:
                # Fill path cells with brown
                pygame.draw.rect(surf, BROWN, rect)
            else:
                pygame.draw.rect(surf, GRAY, rect, 1)


def main():
    clock = pygame.time.Clock()
    run = True

    health = STARTING_HEALTH
    score = STARTING_SCORE
    money = STARTING_MONEY

    towers = []
    enemies = []
    bullets = []

    spawn_timer = 0
    frame_count = 0

    damage_flash_timer = 0  # frames to show flash after damage

    while run:
        clock.tick(FPS)
        frame_count += 1

        # Spawn enemies periodically
        spawn_timer += 1
        if spawn_timer > 120:  # Every 2 seconds at 60 FPS
            chosen_path = random.choice(ALL_PATHS)
            enemies.append(Enemy(chosen_path))
            spawn_timer = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                gx = mx // GRID_SIZE
                gy = my // GRID_SIZE
                # Check if cell is free and not on path
                if (gx, gy) not in ALL_PATH_CELLS:
                    if all(not (t.grid_x == gx and t.grid_y == gy) for t in towers):
                        if event.button == 1:  # Left click for Fast Tower
                            if money >= FAST_TOWER_COST:
                                towers.append(Tower(gx, gy, FAST_TOWER_DAMAGE, FAST_TOWER_FIRE_RATE, FAST_TOWER_COST))
                                money -= FAST_TOWER_COST
                        elif event.button == 3:  # Right click for Slow Tower
                            if money >= SLOW_TOWER_COST:
                                towers.append(Tower(gx, gy, SLOW_TOWER_DAMAGE, SLOW_TOWER_FIRE_RATE, SLOW_TOWER_COST))
                                money -= SLOW_TOWER_COST

        # Update enemies
        enemies_to_remove = []
        for e in enemies:
            e.update()
            if e.reached_end():
                # Enemy reached the base - deal damage
                health -= 1
                damage_flash_timer = 15  # flash for 15 frames
                enemies_to_remove.append(e)
            elif not e.is_alive():
                score += 1
                enemies_to_remove.append(e)
                # Maybe reward some money per kill
                money += 10
        for e in enemies_to_remove:
            if e in enemies:
                enemies.remove(e)

        # Towers shoot bullets
        for t in towers:
            if t.can_shoot(frame_count):
                t.shoot(enemies, frame_count, bullets)

        # Update bullets
        bullets_to_remove = []
        for b in bullets:
            b.update()
            bullet_rect = b.get_rect()
            hit_enemy = None
            for en in enemies:
                if en.is_alive() and bullet_rect.colliderect(en.get_rect()):
                    en.health -= b.damage
                    hit_enemy = en
                    break
            if hit_enemy or b.off_screen():
                bullets_to_remove.append(b)
        for b in bullets_to_remove:
            if b in bullets:
                bullets.remove(b)

        # Check if game is over
        if health <= 0:
            run = False

        # Drawing
        WIN.fill(WHITE)
        draw_grid(WIN)

        for t in towers:
            t.draw(WIN)
        for e in enemies:
            e.draw(WIN)
        for b in bullets:
            b.draw(WIN)

        # Draw HUD
        health_text = FONT.render(f"Health: {health}", True, BLACK)
        score_text = FONT.render(f"Score: {score}", True, BLACK)
        money_text = FONT.render(f"Money: {money}", True, BLACK)
        tower_info_text = FONT.render("Left-click: Fast Tower (50), Right-click: Slow Tower (100)", True, BLACK)
        WIN.blit(health_text, (10, 10))
        WIN.blit(score_text, (10, 30))
        WIN.blit(money_text, (10, 50))
        WIN.blit(tower_info_text, (10, 70))

        # Damage flash
        if damage_flash_timer > 0:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill(FLASH_COLOR)
            WIN.blit(overlay, (0,0))
            damage_flash_timer -= 1

        pygame.display.flip()

    # Game over screen
    WIN.fill(WHITE)
    game_over_text = FONT.render("Game Over! Press any key to exit.", True, BLACK)
    final_score_text = FONT.render(f"Final Score: {score}", True, BLACK)
    WIN.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 20))
    WIN.blit(final_score_text, (WIDTH//2 - final_score_text.get_width()//2, HEIGHT//2 + 20))
    pygame.display.flip()

    # Wait for exit
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
