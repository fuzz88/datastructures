from trie import Trie
import argparse


trie = Trie()
parser = argparse.ArgumentParser(description='Builds and then searches a\
                                              Trie datastructure.')
parser.add_argument('file', type=str,
                    help="The location with a list of newline\
                    delimited words.")
parser.add_argument("word", type=str,
                    help="The word to query through the trie.")
args = parser.parse_args()
print("Building the trie data structure...")
with open(args.file, 'r') as reader:
    for word in reader:
        trie.insert(word.rstrip())
print("Trie data structure built...")
print('Searching the word "{}"...'.format(args.word))

if trie.find_word(args.word):
    print("Word was found in the trie")
else:
    print("Word was not found in the trie")
