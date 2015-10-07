import re


class Node:
    def __init__(self):
        self.item = ''
        self.p = [None, None]


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.found = []

    def insert(self, word):
        """
        Creates the root node, then uses _insert after any additional node
        added.
        """
        if self.root is not None:
            self._insert(self.root, word)
        else:
            self.root = Node()
            self.root.item = word

    def _insert(self, node, word):
        """
        _insert uses recursion until it finds the end of a branch.
        """
        if word < node.item:
            if node.p[0] is not None:
                self._insert(node.p[0], word)
            else:
                node.p[0] = Node()
                node.p[0].item = word
        else:
            if node.p[1] is not None:
                self._insert(node.p[1], word)
            else:
                node.p[1] = Node()
                node.p[1].item = word

    def search(self, word):
        """
        Search passed a string to be regex compiled. That pattern will
        be matched with every word in the tree.
        """
        pattern = re.compile(word)
        if self.root is not None:
            if pattern.fullmatch(self.root.item) is not None:
                self.found.append(self.root.item)
            else:
                self.found.append(self._search(self.root.p[0], word, pattern))
                self.found.append(self._search(self.root.p[1], word, pattern))
        return self.found

    def _search(self, node, word, pattern):
        """
        Recursively travels through the tree looking for a match word.
        """
        if node is not None:
            if pattern.fullmatch(node.item) is not None:
                return node.item
            else:
                self.found.append(self._search(node.p[0], word, pattern))
                self.found.append(self._search(node.p[1], word, pattern))
