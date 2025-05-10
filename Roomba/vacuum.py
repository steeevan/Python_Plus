from astar import astar_search
import random

class Vacuum:
    def __init__(self, room):
        self.room = room
        self.row = 0
        self.col = 0
        self.path = []

    def get_position(self):
        return (self.row, self.col)

    def plan_path(self):
        dirty_tiles = self.room.get_dirty_positions()
        if not dirty_tiles:
            return
        start = (self.row, self.col)
        nearest = min(dirty_tiles, key=lambda pos: abs(pos[0] - self.row) + abs(pos[1] - self.col))
        self.path = astar_search(self.room, start, nearest)

    def move(self):
        if not self.path:
            self.plan_path()
        if self.path:
            self.row, self.col = self.path.pop(0)

    def clean(self):
        if self.room.is_dirty(self.row, self.col):
            self.room.clean(self.row, self.col)
