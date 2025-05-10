import pygame
from game.ball import Ball
from game.paddle import Paddle

class PongGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        self.ball = Ball(320,240,10,5)
        self.player = Paddle(10,200,10,80,6)
        self.ai = Paddle(620,200,10,80,6)

    def reset(self):
        self.ball.reset(320,240)
        self.player.rect.y = 200
        self.ai.rect.y = 200

    
    def step(self,action_ai):
        reward = 0
        done = False

        # move AI paddle 
        if action_ai ==0:
            pass
        elif action_ai == 1:
            self.ai.move(up=True)
        elif action_ai == 2:
            self.ai.move(up=False)
        

        
        keys = pygame.key.get_pressed()

        # Player paddle movement (W/S keys)
        if keys[pygame.K_w]:
            self.player.move(up=True)
        if keys[pygame.K_s]:
            self.player.move(up=False)
        self.ball.move()


        # ball collision
        if self.ball.rect.colliderect(self.player.rect) or self.ball.rect.colliderect(self.ai.rect):
            self.ball.speed_x *= -1

        # score logic
        if self.ball.rect.left <= 0:
            reward  = 1
            done = True
        elif self.ball.rect.right >= 640:
            reward = -1
            done = True
        
        return reward,done

    def render(self):
        self.screen.fill((0,0,0))
        self.ball.draw(self.screen)
        self.player.draw(self.screen)
        self.ai.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(60)

    

        

        