#!/usr/bin/python3

"""Define a node of a singly linked list"""


class Node:
    """class node - defines a node"""

    """
       instantiate with data next_node
       @data: data (int) of the node
       @next_node: next node in the list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """retrieves the data of the node"""
    @property
    def data(self):
        return (self.__data)

    """set the data of the node"""
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """retrieves the node"""
    @property
    def next_node(self):
        return (self.__next_node)

    """set the next node"""
    @next_node.setter
    def next_node(self, value):
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
    Define a singly linked list
"""


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    """
        inserts a new node into correct
        sorted position in the list
    """
    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None:
            """set head to be the new node"""
            new_node.next_node = None
            self.head = new_node
            return

        if self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        tmp = self.head

        while (tmp.next_node is not None and
                tmp.next_node.data < value):
            tmp = tmp.next_node
        new_node.next_node = tmp.next_node
        tmp.next_node = new_node

    """
        print a list in string format
    """
    def __str__(self):
        result = []
        tmp = self.head
        while tmp is not None:
            result.append(str(tmp.data))
            tmp = tmp.next_node

        return ('\n'.join(result))
