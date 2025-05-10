from player import Player

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.move = None

    def set_move(self, square):
        self.move = square

    def get_move(self, board):
        return self.move
