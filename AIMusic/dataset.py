import torch
class NoteDataSet:
    def __init__(self):
        self.notes = ["C", "D", "E", "F", "G", "A", "B"]
        self.vocab = {note: idx for idx, note in enumerate(self.notes)}
        self.ivocab = {idx: note for note, idx in self.vocab.items()}
        self.sequence = ["C", "D", "E", "F", "G", "A", "B"] * 10

    def get_tensor(self):
        idxs = [self.vocab[n] for n in self.sequence]
        input_seq = torch.tensor([idxs[:-1]], dtype=torch.long)
        target_seq = torch.tensor([idxs[1:]], dtype=torch.long)
        return input_seq, target_seq
    
    def vocab_size(self):
        return len(self.vocab)