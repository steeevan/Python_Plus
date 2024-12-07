import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GRAY = (30, 30, 30)
BLUE = (0, 128, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Game variables
money = 500
lives = 20


# Tower class
class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 150
        self.damage = 10
        self.width = 40
        self.height = 40
        self.cooldown = 500  # Time in milliseconds between shots
        self.last_shot = pygame.time.get_ticks()

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x - self.width // 2, self.y - self.height // 2, self.width, self.height))

    def attack(self, enemies, projectiles):
        now = pygame.time.get_ticks()
        if now - self.last_shot >= self.cooldown:
            for enemy in enemies:
                if self.in_range(enemy):
                    # Fire a projectile
                    projectiles.append(Projectile(self.x, self.y, enemy))
                    self.last_shot = now
                    break

    def in_range(self, enemy):
        distance = ((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) ** 0.5
        return distance <= self.range


# Enemy class
class Enemy:
    def __init__(self, path):
        self.path = path
        self.x, self.y = self.path[0]
        self.speed = 2
        self.health = 50
        self.radius = 15
        self.current_path_index = 0

    def update(self):
        if self.current_path_index < len(self.path) - 1:
            target_x, target_y = self.path[self.current_path_index + 1]
            dx, dy = target_x - self.x, target_y - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            if distance <= self.speed:
                self.x, self.y = target_x, target_y
                self.current_path_index += 1
            else:
                self.x += dx / distance * self.speed
                self.y += dy / distance * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), self.radius)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True  # Enemy is dead
        return False


# Projectile class
class Projectile:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target
        self.speed = 5
        self.radius = 5

    def update(self):
        dx, dy = self.target.x - self.x, self.target.y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance <= self.speed:
            # Hit the target
            self.x, self.y = self.target.x, self.target.y
            return True
        else:
            self.x += dx / distance * self.speed
            self.y += dy / distance * self.speed

        return False

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), self.radius)


# Game manager
class GameManager:
    def __init__(self):
        self.towers = [Tower(300, 200), Tower(500, 400)]
        self.enemies = []
        self.projectiles = []
        self.path = [
            (50, 550), (150, 550), (150, 450), (300, 450),
            (300, 300), (600, 300), (600, 100), (750, 100)
        ]

    def update(self):
        for enemy in self.enemies[:]:
            enemy.update()
            if enemy.health <= 0:
                self.enemies.remove(enemy)

        for projectile in self.projectiles[:]:
            if projectile.update():
                # Projectile hit the target
                if projectile.target.take_damage(10):
                    self.enemies.remove(projectile.target)
                self.projectiles.remove(projectile)

        for tower in self.towers:
            tower.attack(self.enemies, self.projectiles)

    def draw(self, screen):
        # Draw the path
        for i in range(len(self.path) - 1):
            pygame.draw.line(screen, WHITE, self.path[i], self.path[i + 1], 3)

        # Draw towers, enemies, and projectiles
        for tower in self.towers:
            tower.draw(screen)

        for enemy in self.enemies:
            enemy.draw(screen)

        for projectile in self.projectiles:
            projectile.draw(screen)

    def add_enemy(self):
        self.enemies.append(Enemy(self.path))


# Main game loop
def main():
    running = True
    game_manager = GameManager()
    spawn_timer = 0

    while running:
        screen.fill(GRAY)  # Background color

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Spawn enemies every 2 seconds
        spawn_timer += clock.get_time()
        if spawn_timer >= 2000:  # 2 seconds
            game_manager.add_enemy()
            spawn_timer = 0

        # Update and draw
        game_manager.update()
        game_manager.draw(screen)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
