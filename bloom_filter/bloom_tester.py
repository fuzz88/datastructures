from bloom import Bloom
import argparse


def replace(word):
    """
    Bad, need a better way.
    """
    if '*' not in word:
        return [word]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    words = []
    for char in word:
        if char == '*':
            for letter in letters:
                words.append(word.replace('*', letter, 1))
                for item in list(words):
                    for char in list(item):
                        if char == '*':
                            for letter in letters:
                                words.append(item.replace('*', letter, 1))
    return words

bloom = Bloom(15000000, 8)
parser = argparse.ArgumentParser(description="Bloom filter. Builds a\
                                 bloom filter. Searches for a word.\
                                 Wildcards(*) allowed.")
parser.add_argument('file', type=str, help="File location")
parser.add_argument('word', type=str, help="Word to search")
args = parser.parse_args()
with open(args.file, 'r') as reader:
    for line in reader:
        bloom.insert(line.rstrip())
print("Bloom filter built.")
print("Searching for \"{}\"...".format(args.word))
if '*' in args.word:
    print("The more wildcards, the longer this takes...")
matches = []
for word in replace(args.word):
    """
    Because how the replacing is done. I check if matches already has
    the word.
    """
    if bloom.find(word) and word not in matches:
        matches.append(word)
print("Results: {}".format(matches))
