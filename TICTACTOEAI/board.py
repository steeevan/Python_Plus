class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            return True
        return False

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def winner(self, square, letter):
        row_index = square // 3
        row = self.board[row_index*3:(row_index+1)*3]
        if all([s == letter for s in row]):
            return True

        col_index = square % 3
        col = [self.board[col_index+i*3] for i in range(3)]
        if all([s == letter for s in col]):
            return True

        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diag1]) or all([s == letter for s in diag2]):
                return True
        return False
