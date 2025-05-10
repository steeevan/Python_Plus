import pygame
import random
from settings import *
from game.paddle import Paddle
from game.ball import Ball
from game.ai_agent import AIAgent
from game.score import Score
from run_manager import RunManager
from logger import Logger
from menu import menu_loop

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Ping Pong AI Menu")

# Initialize menu
font = pygame.font.SysFont("Arial", 24)
game_mode = menu_loop(screen, font)
if game_mode is None:
    pygame.quit()
    exit()

# Game Objects
ball = Ball()
score = Score()
run_manager = RunManager()
logger = Logger(filename="training_log_agents.csv")

# Define paddles
player_left = Paddle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, is_ai=False)
ai_left = Paddle(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, is_ai=True)
ai_right = Paddle(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, is_ai=True)

# Determine game setup
agent_left = None
agent_right = None
player_controlled = False

if game_mode == 1:
    # Player vs AI 1
    agent_right = AIAgent(ai_right, ball, name="ai_1", training_mode=True)
    left_paddle = player_left
    right_paddle = ai_right
    player_controlled = True
elif game_mode == 2:
    # Player vs AI 2
    agent_right = AIAgent(ai_right, ball, name="ai_2", training_mode=True)
    left_paddle = player_left
    right_paddle = ai_right
    player_controlled = True
elif game_mode == 3:
    # AI vs AI
    agent_left = AIAgent(ai_left, ball, name="ai_1", training_mode=True)
    agent_right = AIAgent(ai_right, ball, name="ai_2", training_mode=True)
    agent_left.opponent = agent_right
    agent_right.opponent = agent_left
    left_paddle = ai_left
    right_paddle = ai_right

if agent_left:
    agent_left.load()
if agent_right:
    agent_right.load()

training_mode = True
font_small = pygame.font.SysFont("Arial", 18)
shake_timer = 0
shake_offset = [0, 0]
paused = False

running = True
while running:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if agent_left: agent_left.save()
            if agent_right: agent_right.save()
            running = False
        elif event.type == pygame.USEREVENT and event.dict.get('shake'):
            shake_timer = 8
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            elif event.key == pygame.K_r:
                ball.reset()
                if agent_left: agent_left.reset_total_reward()
                if agent_right: agent_right.reset_total_reward()
                score.ai_score = 0
                score.player_score = 0

    if paused:
        screen.blit(font.render("PAUSED - Press P to resume", True, WHITE), (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.flip()
        clock.tick(15)
        continue

    # Shake logic
    if shake_timer > 0:
        shake_offset = [random.randint(-4, 4), random.randint(-4, 4)]
        shake_timer -= 1
    else:
        shake_offset = [0, 0]

    # Player control
    if player_controlled:
        left_paddle.move(keys[pygame.K_w], keys[pygame.K_s])

    # Game logic
    ball.update()
    if agent_left:
        agent_left.update()
    if agent_right:
        agent_right.update()

    ball.check_collision(left_paddle)
    ball.check_collision(right_paddle)

    if ball.x <= 0:
        score.ai_score += 1
        run_manager.increment()
        if agent_right:
            agent_right.reward(+1)
        if agent_left:
            agent_left.reward(-1)
        logger.log(run_manager.run_count, agent_right.get_total_reward() if agent_right else 0, agent_right.get_epsilon() if agent_right else 0, score.ai_score, score.player_score)
        ball.reset()
        if agent_left: agent_left.reset_total_reward()
        if agent_right: agent_right.reset_total_reward()

    elif ball.x >= WIDTH:
        score.player_score += 1
        run_manager.increment()
        if agent_left:
            agent_left.reward(+1)
        if agent_right:
            agent_right.reward(-1)
        logger.log(run_manager.run_count, agent_left.get_total_reward() if agent_left else 0, agent_left.get_epsilon() if agent_left else 0, score.ai_score, score.player_score)
        ball.reset()
        if agent_left: agent_left.reset_total_reward()
        if agent_right: agent_right.reset_total_reward()
    else:
        if agent_left:
            agent_left.reward(0.01)
        if agent_right:
            agent_right.reward(0.01)

    # Drawing
    screen.fill(BLACK)
    draw_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    left_paddle.draw(draw_surface)
    right_paddle.draw(draw_surface)
    ball.draw(draw_surface)
    score.draw(draw_surface)
    run_manager.draw(draw_surface)

    if agent_left:
        agent_left.draw_heatmap(draw_surface, side='left')
    if agent_right:
        agent_right.draw_heatmap(draw_surface, side='right')

    # Display info
    draw_surface.blit(font_small.render(f"Mode: {['None','P vs AI1','P vs AI2','AI vs AI'][game_mode]}", True, WHITE), (10, HEIGHT - 120))
    draw_surface.blit(font_small.render("Press 'P' to Pause | 'R' to Restart", True, WHITE), (10, HEIGHT - 100))
    if agent_left:
        draw_surface.blit(font_small.render(f"Left W/L: {agent_left.wins}/{agent_left.losses}", True, WHITE), (10, HEIGHT - 80))
    if agent_right:
        draw_surface.blit(font_small.render(f"Right W/L: {agent_right.wins}/{agent_right.losses}", True, WHITE), (WIDTH - 180, HEIGHT - 80))

    screen.blit(draw_surface, shake_offset)
    pygame.display.flip()
    clock.tick(90)

pygame.quit()
