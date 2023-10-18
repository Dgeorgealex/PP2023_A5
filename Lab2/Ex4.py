def compose(notes, moves, start):
    size = len(notes)
    current = start
    song = [notes[current]]
    for m in moves:
        current = (current + m + size) % size
        song.append(notes[current])

    return song


if __name__ == "__main__":
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

