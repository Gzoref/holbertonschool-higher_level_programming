#!/usr/bin/python3
"""Singley Linked List"""""


class Node:
    """Node class"""


    def __init__(self, data, next_node=None):
        """Defines a node of LL"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data Getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data Setter"""
        if type(data) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """next_node Getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node Setter"""
        if type(next_node) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    """Singley Linked List class"""

    node = Node()

    def __init__(self):
        self.__head = head


    def sorted_insert(self, value):
        """Inserts a new node at sorted position"""
        new_node = Node(value)
        new_node.next_node(self.head)
        self.head = next_node

        while new_node.next_node is not None:
            print('{}'.format(new_node.data))
