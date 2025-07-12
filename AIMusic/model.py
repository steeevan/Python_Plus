import torch.nn as nn

class MusicLSTM(nn.Module):
    def __init__(self,vocab_size,hidden_size=128):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, 128)
        self.lstm =nn.LSTM(128,hidden_size,batch_first=True)
        self.fc = nn.Linear(hidden_size,vocab_size)

    def forward(self,x,hidden=None):
        x = self.embed(x)
        out, hidden = self.lstm(x,hidden)
        out = self.fc(out)
        return out, hidden
    


