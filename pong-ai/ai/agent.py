'''
A neural network (LinearQnet) to predict the best action given a game state

Epsilon-greedy exploration to balance random moves and learned moved

A memory buffer ( dequue ) to store past experiences ( state, action, reward, nex state, etc)

'''
import torch
import random
import numpy as np
from collections import deque
from ai.model import LinearQNet
# setup
MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0 # exploration factor
        self.gamma = 0.9 # discount factor
        self.memory = deque(maxlen=MAX_MEMORY)
        self.model = LinearQNet(6,256,3)
        self.optimizer = torch.optim.Adam(self.model.parameters(),lr=LR)

    def get_state(self,game):
        ball = game.ball
        paddle = game.paddle2


        state = [
            ball.rect.x / game.WIDTH,
            ball.rect.y / game.HEIGHT,
            ball.x_vel / 10,
            ball.y_vel / 10,
            paddle.rect.y / game.HEIGHT,
            (paddle.rect.y + paddle.rect.height) / game.HEIGHT
        ]
        return np.array(state,dtype=float)
    


    def remember(self,state,action,reward,next_state,done):
        self.memory.append((state,action,reward,next_state,done))

    
    def train_long_memory(self):
        pass  # Add training logic later

    def train_short_memory(self, state, action, reward, next_state, done):
        pass  # Add training logic later


    def get_action(self,state):
        self.epsilon = 80 - self.n_games
        final_move = [0,0,0]
        if random.randint(0,200) < self.epsilon:
            move = random.randint(0,2)
            final_move[move]= 1
        else:
            state0 = torch.tensor(state,dtype=torch.float)
            prediction = self.model(state0)
            move =torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move