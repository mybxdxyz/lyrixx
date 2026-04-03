import subprocess


def get_artist():
    artist = subprocess.run(
        ["playerctl", "metadata", "artist"], capture_output=True, text=True
    )
    return artist.stdout.strip()


def get_title():
    title = subprocess.run(
        ["playerctl", "metadata", "title"], capture_output=True, text=True
    )
    return title.stdout.strip()


def get_pos():
    pos = subprocess.run(["playerctl", "position"], capture_output=True, text=True)
    return float(pos.stdout.strip())
