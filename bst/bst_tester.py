import argparse
from bst import BinarySearchTree


if __name__ == "__main__":
    def replace(string):
        """
        Search uses regex for searching with wildcards.
        The . (dot) is any char.
        """
        return string.replace('*', '.', 25)

    parser = argparse.ArgumentParser(description="Binary Search Tree. Builds\
                                     a tree from a file containing a list of\
                                     words. Then searches that tree for the\
                                     inputed word. Wildcards(*) are allowed.")
    parser.add_argument('file', type=str, help="File location")
    parser.add_argument('word', type=str, help="Word to search")
    args = parser.parse_args()
    search_value = replace(args.word)
    with open(args.file, 'r') as reader:
            print("Building binary search tree...")
            bst = BinarySearchTree()
            for line in reader:
                bst.insert(line.rstrip())
    words = bst.search(search_value)
    """
    There's a issue in the bst search function that returns None.
    Lazy fix is list comprehension to remove all Nones.
    """
    words = [word for word in words if word is not None]
    print("Following words were matched: \n" + str(words))
