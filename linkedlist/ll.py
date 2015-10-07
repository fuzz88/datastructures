import re


class Node:
    def __init__(self):
        self.item = ''
        self.p = [None, None]


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, word):
        if self.head is None:
            self.head = Node()
            self.head.item = word
        new_node = Node()
        new_node.item = word
        new_node.p[1] = self.head
        self.head = new_node

    def search(self, value):
        reg_value = re.compile(value)
        current = self.head
        found = []
        while current is not None:
            if reg_value.fullmatch(current.item) is not None:
                found.append(current.item)
            current = current.p[1]
        return found
