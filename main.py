import player
import fetch
import parse
import visual
import time
import bisect
import os


def load_song():
    current_artist = player.get_artist()
    current_track = player.get_title()
    current_song = fetch.fetchem(current_artist, current_track)
    lyrics = parse.lrc_parse(current_song)
    timestamps = [t for t, _ in lyrics]
    return lyrics, timestamps, current_track


lyrics, timestamps, current_track = load_song()

previous_lyric = ""
previous_track = ""
current_lyric = ""

while True:
    position = player.get_pos() * 1000
    current_track = player.get_title()

    if previous_track != current_track:
        lyrics, timestamps, current_track = load_song()
        previous_track = current_track

    i = bisect.bisect_right(timestamps, position) - 1

    if i >= 0:
        current_lyric = lyrics[i][1]

    if current_lyric != previous_lyric:
        os.system("cls" if os.name == "nt" else "clear")
        visual.render(current_lyric)
        previous_lyric = current_lyric

    time.sleep(0.05)
