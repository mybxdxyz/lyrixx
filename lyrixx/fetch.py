import requests


def fetchem(artist, title):
    url = "https://lrclib.net/api/get?"
    params = dict(artist_name=artist, track_name=title)
    fetch = requests.get(url=url, params=params)
    data = fetch.json()
    return data["syncedLyrics"]
