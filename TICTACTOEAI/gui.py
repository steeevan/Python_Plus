import tkinter as tk
from human_player import HumanPlayer
from ai_player import AIPlayer
from board import Board
from game import Game

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe AI")

        self.x_score = 0
        self.o_score = 0
        self.tie_score = 0

        # Game Objects
        self.board = Board()
        self.human = HumanPlayer('X')
        self.ai = AIPlayer('O')
        self.game = Game(self.board, self.human, self.ai)

        # UI Elements
        self.status_label = tk.Label(self.window, text="Welcome to Tic Tac Toe!", font=('Arial', 20))
        self.status_label.grid(row=0, column=0, columnspan=3)

        self.score_label = tk.Label(self.window, text=self.get_score_text(), font=('Arial', 16))
        self.score_label.grid(row=1, column=0, columnspan=3)

        self.buttons = []
        self.build_grid()

        self.reset_btn = tk.Button(self.window, text="Reset", font=('Arial', 14), command=self.reset_game)
        self.reset_btn.grid(row=5, column=0, columnspan=3, pady=10)

        self.window.mainloop()

    def build_grid(self):
        for i in range(9):
            button = tk.Button(self.window, text='', font=('Arial', 32), width=5, height=2,
                               command=lambda i=i: self.human_move(i))
            button.grid(row=(i // 3) + 2, column=i % 3)  # +2 to offset the title and score rows
            self.buttons.append(button)

    def get_score_text(self):
        return f"Score - X: {self.x_score} | O: {self.o_score} | Ties: {self.tie_score}"

    def human_move(self, i):
        if self.board.board[i] == ' ':
            self.human.set_move(i)
            square = self.human.get_move(self.board)
            letter, win = self.game.play_turn(square)
            self.update_button(i, letter)
            if win:
                self.end_game(f"{letter} wins!")
                return
            if not self.board.empty_squares():
                self.end_game("It's a tie!")
                return
            self.window.after(500, self.ai_move)

    def ai_move(self):
        square = self.ai.get_move(self.board)
        letter, win = self.game.play_turn(square)
        self.update_button(square, letter)
        if win:
            self.end_game(f"{letter} wins!")
        elif not self.board.empty_squares():
            self.end_game("It's a tie!")

    def update_button(self, i, letter):
        self.buttons[i].config(text=letter, state="disabled")

    def end_game(self, message):
        self.status_label.config(text=message)
        if message == "It's a tie!":
            self.tie_score += 1
        elif "X" in message:
            self.x_score += 1
        elif "O" in message:
            self.o_score += 1

        self.score_label.config(text=self.get_score_text())

        for button in self.buttons:
            button.config(state='disabled')

    def reset_game(self):
        self.board = Board()
        self.human = HumanPlayer('X')
        self.ai = AIPlayer('O')
        self.game = Game(self.board, self.human, self.ai)

        for button in self.buttons:
            button.config(text='', state='normal')

        self.status_label.config(text="New Game!")
