import player
import fetch
import parse
import visual
import time
import bisect
import os

artist = player.get_artist()
track = player.get_title()
current_song = fetch.fetchem(artist, track)
lyrics = parse.lrc_parse(current_song)
timestamps = [t for t, _ in lyrics]
previous_lyric = ""
current_lyric = ""

while True:
    position = player.get_pos() * 1000
    i = bisect.bisect_right(timestamps, position) - 1
    if i >= 0:
        current_lyric = lyrics[i][1]
    if current_lyric != previous_lyric:
        os.system("cls" if os.name == "nt" else "clear")
        visual.render(current_lyric)
        previous_lyric = current_lyric
    time.sleep(0.05)
