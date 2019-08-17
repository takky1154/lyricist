import random


class MarkovChain:
    def __init__(self, wordlist: list):
        self.wordlist = wordlist
        self.chain = {}
        self._generate_chain()

    def _generate_chain(self):
        for i, word in enumerate(self.wordlist):
            if len(self.wordlist) > i + 2:
                key = tuple(self.wordlist[i:i + 2])

                next_word = self.wordlist[i + 2]

                if key in self.chain:
                    self.chain[key].append(next_word)
                else:
                    self.chain[key] = [next_word]
            i += 1

    def generate_text(self, num_words: int):
        current_words = random.choice(list(self.chain))
        text = current_words[0].upper() + ' ' + current_words[1]

        for i in range(1, num_words):
            next_word = random.choice(self.chain[current_words])
            current_words = (current_words[1], next_word)

            # Ensures that there is no extra space before a comma.

            if next_word == '':
                continue
            elif next_word == ',':
                text += next_word
            else:
                text += ' ' + next_word
        return text
