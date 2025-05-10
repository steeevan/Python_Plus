import random

class Room:
    def __init__(self, rows, cols, dirt_prob=0.2):
        self.rows = rows
        self.cols = cols
        self.grid = [[1 if random.random() < dirt_prob else 0 for _ in range(cols)] for _ in range(rows)]

    def is_dirty(self, row, col):
        return self.grid[row][col] == 1

    def clean(self, row, col):
        self.grid[row][col] = 0

    def all_clean(self):
        return all(cell == 0 for row in self.grid for cell in row)

    def get_dirty_positions(self):
        return [(r, c) for r in range(self.rows) for c in range(self.cols) if self.grid[r][c] == 1]
