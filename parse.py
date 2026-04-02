def conversion(timestamp):
    mins = timestamp.split(":")
    ms = mins[1].split(".")
    return (int(mins[0]) * 60 + int(ms[0])) * 1000 + int(ms[1]) * 10


def lrc_parse(txt):
    output = []
    lines = txt.splitlines()
    for line in lines:
        if line[1].isdigit():
            part = line.split("]")
            timestamp = part[0][1:]
            lyric = part[1]
            output.append((conversion(timestamp), lyric.strip()))
    return output
