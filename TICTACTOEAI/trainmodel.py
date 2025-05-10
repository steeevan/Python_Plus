import torch
import torch.nn as nn
import torch.optim as optim
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

def generate_training_data(n=5000):
    X = []
    y = []
    for _ in range(n):
        board = [random.choice([0, 1, -1]) for _ in range(9)]
        label = random.randint(0, 8)
        X.append(board)
        y.append(label)
    return torch.tensor(X, dtype=torch.float32), torch.tensor(y, dtype=torch.long)

def train():
    model = TicTacToeModel()
    X, y = generate_training_data()
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(10):
        optimizer.zero_grad()
        output = model(X)
        loss = loss_fn(output, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), 'TICTACTOEAI/model/ai_model.pth')

if __name__ == '__main__':
    train()
