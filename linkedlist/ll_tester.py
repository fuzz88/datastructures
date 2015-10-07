import argparse
from ll import LinkedList

if __name__ == "__main__":
    def replace(string):
        """
        Search uses regex for searching with wildcards.
        The . (dot) is any char.
        """
        return string.replace('*', '.', 25)

    parser = argparse.ArgumentParser(description="Linked list. Builds\
                                     a list from a file containing a list of\
                                     words. Then searches that list for the\
                                     inputed word. Wildcards(*) are allowed.")
    parser.add_argument('file', type=str, help="File location")
    parser.add_argument('word', type=str, help="Word to search")
    args = parser.parse_args()
    search_value = replace(args.word)
    with open(args.file, 'r') as reader:
        print("Building linked list...")
        linked_list = LinkedList()
        for line in reader:
            linked_list.insert(line.rstrip())
    query = str(linked_list.search(search_value))
    print("The following words were matched: \n" + query)
