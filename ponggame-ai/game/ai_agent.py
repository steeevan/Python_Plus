from training.q_learning_trainer import QLearningTrainer
import pygame
from settings import WIDTH, HEIGHT

class AIAgent:
    def __init__(self, paddle, ball, name="agent", training_mode=True, opponent=None):
        self.name = name
        self.paddle = paddle
        self.ball = ball
        self.training_mode = training_mode
        self.trainer = QLearningTrainer(filename=f"{self.name}_q_table.pkl")
        self.last_state = None
        self.last_action = None
        self.heatmap = [0 for _ in range(HEIGHT)]
        self.opponent = opponent  # opponent agent for multi-agent learning
        self.wins = 0
        self.losses = 0

    def update(self):
        state = self.trainer.discretize_state(
            self.paddle.rect.centery,
            self.ball.x,
            self.ball.y,
            self.ball.dx,
            self.ball.dy
        )

        action = self.trainer.get_action(state, force_best=not self.training_mode)

        target_y = self.ball.y
        if action == 'up':
            self.paddle.move_toward(target_y - 20)
        elif action == 'down':
            self.paddle.move_toward(target_y + 20)
        else:
            self.paddle.move_toward(target_y)

        self.last_state = state
        self.last_action = action

        # Update heatmap
        paddle_y = self.paddle.rect.centery
        if 0 <= paddle_y < HEIGHT:
            self.heatmap[int(paddle_y)] += 1

    def reward(self, value):
        next_state = self.trainer.discretize_state(
            self.paddle.rect.centery,
            self.ball.x,
            self.ball.y,
            self.ball.dx,
            self.ball.dy
        )
        self.trainer.update(self.last_state, self.last_action, value, next_state)

        # Multi-agent feedback with win/loss tracking
        if self.opponent and self.training_mode:
            if value > 0:
                self.wins += 1
                self.opponent.losses += 1
                self.opponent.trainer.update(self.opponent.last_state, self.opponent.last_action, -1, next_state)
            elif value < 0:
                self.losses += 1
                self.opponent.wins += 1
                self.opponent.trainer.update(self.opponent.last_state, self.opponent.last_action, +1, next_state)

    def save(self):
        self.trainer.save_q_table()

    def load(self):
        self.trainer.load_q_table()

    def reset_total_reward(self):
        self.trainer.reset_reward()

    def get_total_reward(self):
        return self.trainer.get_total_reward()

    def get_epsilon(self):
        return self.trainer.epsilon

    def draw_heatmap(self, screen, side='left'):
        max_value = max(self.heatmap) if max(self.heatmap) > 0 else 1
        for y, value in enumerate(self.heatmap):
            intensity = int((value / max_value) * 255)
            color = (intensity, intensity, 50)
            x_pos = 5 if side == 'left' else WIDTH - 10
            pygame.draw.line(screen, color, (x_pos, y), (x_pos + 3, y))
