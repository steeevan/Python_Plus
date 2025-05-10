import random

class SimpleTrainer:
    def __init__(self):
        self.learning_rate = 0.1
        self.discount = 0.9
        self.epsilon = 0.1  # exploration rate
        self.q_table = {}   # state-action values

    def get_state(self, paddle_y, ball_y):
        return (round(paddle_y / 10), round(ball_y / 10))

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(['up', 'down', 'stay'])

        if state not in self.q_table:
            self.q_table[state] = {'up': 0, 'down': 0, 'stay': 0}

        return max(self.q_table[state], key=self.q_table[state].get)

    def update(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = {'up': 0, 'down': 0, 'stay': 0}
        if next_state not in self.q_table:
            self.q_table[next_state] = {'up': 0, 'down': 0, 'stay': 0}

        old_value = self.q_table[state][action]
        future_max = max(self.q_table[next_state].values())

        new_value = old_value + self.learning_rate * (reward + self.discount * future_max - old_value)
        self.q_table[state][action] = new_value
