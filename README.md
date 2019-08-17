# Lyricist
Generate your own lyrics!

The idea for this project comes from https://github.com/iluxonchik/lyricist
That project no longer works though (presumably from Genius site changes breaking the scraping functionality), so I decided to create my own.

# Usage

In order to download and generate lyrics, 2 files must be run.

``download_songs.py``
and
``generate.py``
```
usage: download_lyrics.py [-h] [--dir DIR] [-n N] artist

positional arguments:
  artist      Artist to download lyrics from

optional arguments:
  -h, --help  show this help message and exit
  --dir DIR   Directory to download lyrics to (defaults to artist name)
  -n N        Number of songs to download (default: 10)
```
```
usage: generate.py [-h] [-n N] [-o O] file

This program allows you to generate lyrics based on lyrics scraped from Genius

positional arguments:
  file        File to use as source

optional arguments:
  -h, --help  show this help message and exit
  -n N        Number of words to output (default 100)
  -o O        File to write output to (default: output.txt)
```

``download_songs.py`` creates a '.txt' file with all of the lyrics downloaded.
The name of the file defaults to the name of the artist (Ex: "Michael Jackson.txt"), but it can be specified using ``--dir``

You then run ``generate.py`` using the file that was just created.
***Example***: ``python generate.py "Michael Jackson.txt"``
