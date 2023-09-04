#!/usr/bin/python3

"""Define a node of a singly linked list"""


class Node:

    """
       instantiate with data & next_node
       @data: data (int) of the node
       @next_node: next node in the list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data attribute"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set the data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Get the next_node attribute"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set the next_node attribute"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize an empty SLL"""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new node with a given
           value into the sorted position
           in the list
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head

        while (current.next_node and current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """convert the list to a printable string"""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node

        return ('\n'.join(result))
