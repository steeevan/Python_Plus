class Game:
    def __init__(self, board, x_player, o_player):
        self.board = board
        self.x_player = x_player
        self.o_player = o_player
        self.current_letter = 'X'

    def play_turn(self, square):
        if self.board.make_move(square, self.current_letter):
            winner = self.board.winner(square, self.current_letter)
            current = self.current_letter
            self.current_letter = 'O' if self.current_letter == 'X' else 'X'
            return current, winner
        return None, False
