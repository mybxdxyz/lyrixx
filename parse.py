def conversion(timestamp):
    mins = timestamp.split(":")
    ms = mins[1].split(".")
    return (int(mins[0]) * 60 + int(ms[0])) * 1000 + int(ms[1]) * 10


def lrc_parse(txt):
    output = []
    lines = txt.splitlines()
    raw = []
    for line in lines:
        if line[1].isdigit():
            part = line.split("]")
            timestamp = conversion(part[0][1:])
            lyric = part[1].strip()
            raw.append((timestamp, lyric))

    for i, (timestamp, lyric) in enumerate(raw):
        words = lyric.split()
        if not words:
            continue
        if i + 1 < len(raw):
            next_timestamp = raw[i + 1][0]
        else:
            next_timestamp = timestamp + 3000
        duration = next_timestamp - timestamp
        per_word = duration // len(words)
        for j, word in enumerate(words):
            output.append((timestamp + j * per_word, word))

    return output
