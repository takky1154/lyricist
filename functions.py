import os
import json
import re


def write_lyrics(directory: str, file_name):
    """
    Takes all lyrics from each downloaded file
    and inserts them into a single file
    """
    for song in os.listdir(directory):
        with open(directory + '/' + song, 'r', encoding='utf-8', errors='ignore') as lyrics:
            with open(file_name, 'a+', errors='ignore') as f:
                lyrics = json.loads(lyrics.read())
                f.write(lyrics['songs'][0]['lyrics'])


def clean_file(file_name: str):
    """
    Removes all [Chorus]  and [Verse] lines
    while also removing double line breaks
    And puts spaces between each comma and period so that they are treated as words by the chain generator
    """
    with open(file_name, 'r+') as f:
        text = f.read()
        new = re.sub(r'\[.*?\]', '', text).replace('\n\n', '\n').replace(',', ' ,').replace('.', ' .')
        f.seek(0)
        f.truncate()
        f.write(new)


def read_file(file_name: str):
    with open(file_name, 'r') as f:
        text = f.read().replace('\n\n', ' ').replace(',', ' ,').replace('.', ' .')
    return text
