import argparse
import lyricsgenius
from markov import MarkovChain
from functions import *

access_token = "0odksUYV1SxnSkQJ8bv4V20HH4M9rPozkeCruvFkVPlBBlfuNskw2R1wk1u5m7J5"

genius = lyricsgenius.Genius(access_token)

description = "This program allows you to generate lyrics based on lyrics scraped from Genius"
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-n', type=int, help="Number of words to output (default 100)", default=100)
parser.add_argument('-o', type=str, help="File to write output to (default: output.txt)", default='output.txt')
parser.add_argument('file', type=str, help="File to use as source")
args = parser.parse_args()


def generate_text(input, output):
    if os.path.isfile(args.o):
        os.remove(args.o)
    num_words = args.n

    contents = read_file(input)
    wordlist = contents.split(' ')

    markov = MarkovChain(wordlist)

    with open(output, 'a+') as f:
        f.write(markov.generate_text(num_words))


if __name__ == '__main__':
    generate_text(args.file, args.o)
