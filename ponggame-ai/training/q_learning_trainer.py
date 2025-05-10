import random
import pickle
import os

class QLearningTrainer:
    def __init__(self, state_bins=(12, 12), actions=('up', 'down', 'stay'), alpha=0.1, gamma=0.95, epsilon=1.0, filename="q_table.pkl"):
        self.state_bins = state_bins
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = 0.995
        self.min_epsilon = 0.01
        self.q_table = {}
        self.total_reward = 0
        self.filename = filename

    def discretize_state(self, paddle_y, ball_x, ball_y, ball_dx, ball_dy):
        paddle_bin = min(int(paddle_y / 600 * self.state_bins[0]), self.state_bins[0] - 1)
        ball_x_bin = min(int(ball_x / 800 * self.state_bins[0]), self.state_bins[0] - 1)
        ball_y_bin = min(int(ball_y / 600 * self.state_bins[1]), self.state_bins[1] - 1)

        dx = 1 if ball_dx > 0 else -1
        dy = 1 if ball_dy > 0 else -1

        # Additional AI awareness
        distance_y = int((ball_y - paddle_y) / 50)
        distance_y = max(-3, min(3, distance_y))

        speed = (abs(ball_dx) + abs(ball_dy)) / 2
        if speed < 5:
            speed_level = 0
        elif speed < 9:
            speed_level = 1
        else:
            speed_level = 2

        return (paddle_bin, ball_x_bin, ball_y_bin, dx, dy, distance_y, speed_level)

    def get_action(self, state, force_best=False):
        if (not force_best) and (random.random() < self.epsilon or state not in self.q_table):
            return random.choice(self.actions)

        return max(self.q_table[state], key=self.q_table[state].get)

    def update(self, state, action, reward, next_state):
        self.total_reward += reward

        if state not in self.q_table:
            self.q_table[state] = {a: 0.0 for a in self.actions}
        if next_state not in self.q_table:
            self.q_table[next_state] = {a: 0.0 for a in self.actions}

        old_value = self.q_table[state][action]
        future_max = max(self.q_table[next_state].values())
        new_value = old_value + self.alpha * (reward + self.gamma * future_max - old_value)
        self.q_table[state][action] = new_value

        self.epsilon = max(self.epsilon * self.epsilon_decay, self.min_epsilon)

    def save_q_table(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.q_table, f)

    def load_q_table(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as f:
                self.q_table = pickle.load(f)

    def reset_reward(self):
        self.total_reward = 0

    def get_total_reward(self):
        return self.total_reward