import torch
import torch.nn as nn
from player import Player
from board import Board
import random

class TicTacToeModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(9, 64),
            nn.ReLU(),
            nn.Linear(64, 9)
        )

    def forward(self, x):
        return self.net(x)

class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        self.model = TicTacToeModel()
        self.model.load_state_dict(torch.load("TICTACTOEAI/model/ai_model.pth"))
        self.model.eval()

    def encode_board(self, board_obj):
        encoding = []
        for cell in board_obj.board:
            if cell == self.letter:
                encoding.append(1)
            elif cell == ' ':
                encoding.append(0)
            else:
                encoding.append(-1)
        return torch.tensor(encoding, dtype=torch.float32)

    def get_move(self, board_obj):
        board_tensor = self.encode_board(board_obj)
        with torch.no_grad():
            logits = self.model(board_tensor)
            probs = logits.softmax(dim=0)
            sorted_moves = probs.argsort(descending=True)
            for move in sorted_moves:
                move = move.item()
                if board_obj.board[move] == ' ':
                    return move
        return random.choice(board_obj.available_moves())
