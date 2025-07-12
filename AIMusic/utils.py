import pretty_midi

def save_midi(note_list, filename="generated.mid"):
    midi = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=0)
    note_map = {
        "C": 60, "D": 62, "E": 64,
        "F": 65, "G": 67, "A": 69, "B": 71
    }

    start = 0
    for n in note_list:
        pitch = note_map[n]
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start+0.5)
        instrument.notes.append(note)
        start += 0.5

    midi.instruments.append(instrument)
    midi.write(filename)
