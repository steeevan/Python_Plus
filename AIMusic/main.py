from model import MusicLSTM
from dataset import NoteDataSet
from generate import generate_music
from utils import save_midi
import torch
import torch.nn as nn
import torch.optim as optim

# Load dataset
dataset = NoteDataSet()
input_seq, target_seq = dataset.get_tensor()

# Initialize model
model = MusicLSTM(dataset.vocab_size())
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
for epoch in range(300):
    model.train()
    optimizer.zero_grad()
    output, _ = model(input_seq)
    loss = criterion(output.squeeze(0), target_seq.squeeze(0))
    loss.backward()
    optimizer.step()
    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# Generate music
generated = generate_music(model, dataset, seed="C", length=40)
print("Generated:", generated)

# Save to MIDI
save_midi(generated)
