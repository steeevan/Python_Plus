import torch

def generate_music(model, dataset, seed="C", length=30):
    model.eval()
    idx = dataset.vocab[seed]
    input_seq = torch.tensor([[idx]], dtype=torch.long)
    hidden = None
    output = [seed]

    for _ in range(length):
        logits, hidden = model(input_seq, hidden)
        prob = torch.softmax(logits[0, -1], dim=0)
        idx = torch.multinomial(prob, 1).item()
        output.append(dataset.ivocab[idx])
        input_seq = torch.tensor([[idx]], dtype=torch.long)

    return output
