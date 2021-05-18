#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """This initializes the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This is a getter for data"""
        return self.__data

    @data.setter
    def data(self, data):
        """This is a setter for data"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """This is a getter for the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """This is a setter for the next node"""
        if type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """This initializes the list"""
        self.head = None

    def __repr__(self):
        string = ""
        if self.head is None:
            pass
        else:
            placeholder = self.head
            while placeholder is not None:
                string += str(placeholder.data)
                string += '\n'
                placeholder = placeholder.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """inserts a new Node into the correct position in the list"""
        new_node = Node(value)
        current = self.head
        if current is None:
            self.head = new_node
        elif value < current.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            while current.next_node is not None and\
            current.next_node.data < value:
                current = current.next_node
            if current.next_node is None:
                current.next_node = new_node
            else:
                current.next_node = Node(value, current.next_node)
