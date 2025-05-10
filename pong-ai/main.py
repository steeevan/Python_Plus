from game.game import PongGame
import pygame
import sys

game = PongGame()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    action = 0 # replace later with AI agent 
    reward, done = game.step(action)
    game.render()

    if done:
        game.reset()