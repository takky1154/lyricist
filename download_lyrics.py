import lyricsgenius
import argparse
from functions import *

parser = argparse.ArgumentParser()
parser.add_argument("artist", type=str, help="Artist to download lyrics from")
parser.add_argument('--dir', type=str, help="Directory to download lyrics to (defaults to artist name)")
parser.add_argument('-n', type=int, help="Number of songs to download (default: 10", default=10)
args = parser.parse_args()

if not args.dir:
    args.dir = args.artist

lyrics_file = args.dir + '.txt'
genius = lyricsgenius.Genius("0odksUYV1SxnSkQJ8bv4V20HH4M9rPozkeCruvFkVPlBBlfuNskw2R1wk1u5m7J5")

if args.dir:
    if not os.path.isdir(args.dir):
        os.mkdir(args.dir)
        os.chdir(args.dir)
    else:
        os.chdir(args.dir)

artist = genius.search_artist(args.artist, max_songs=args.n)
artist.save_lyrics()
os.chdir('..')

write_lyrics(args.dir, lyrics_file)
clean_file(lyrics_file)
