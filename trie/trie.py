class Node(object):
    def __init__(self, letter):
        self.pointers = list()
        self.letter = letter
        self.end_of_word = False


class Trie(object):
    def __init__(self):
        self.root = Node("")
        self.current_node = self.root

    def insert(self, word):
        self.current_node = self.root
        for letter in word:
            self.current_node = self.__insert_letter(letter)
        self.current_node.end_of_word = True

    def __insert_letter(self, letter):
        for node in self.current_node.pointers:
            if node.letter == letter:
                return node
        new_node = Node(letter)
        self.current_node.pointers.append(new_node)
        return new_node

    def find_word(self, word):
        self.current_node = self.root
        for letter in word:
            for node in self.current_node.pointers:
                if node.letter == letter:
                    self.current_node = node
                    break
            else:
                return False
        return self.current_node.end_of_word
