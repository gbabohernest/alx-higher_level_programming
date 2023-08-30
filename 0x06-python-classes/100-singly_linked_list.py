#!/usr/bin/python3

"""Define a node of a
   singly linked list
"""


class Node:
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
        return self.__data

    """set the data of the node"""
    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    """retrieves the node"""
    @property
    def next_node(self):
        return self.__next_node

    """set the next node"""
    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""
    Define a singly linked list
"""


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    """
        inserts a new node into correct
        sorted position in the list
    """
    def sorted_insert(self, value):
        tmp = self.__head

        if tmp is None or value < tmp.data:
            """set head to be the new node"""
            self.__head = Node(value, tmp)

        else:
            while (tmp.next_node is not None and
                    value >= tmp.next_node.data):
                tmp = tmp.next_node
            tmp.next_node = Node(value, tmp.next_node)

    """
        print a list in string format
    """
    def __str__(self):
        tmp = self.__head
        result = []
        while tmp is not None:
            result.append(str(tmp.data))
            tmp = tmp.next_node

        return "\n".join(result)
