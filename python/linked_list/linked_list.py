from typing import Text


class Node:
    """
    Class for Node implementation with fields for value and pointer

    Fileds :
        None

    Behaviours :
     __init__(data, next_):
        The constructor method for the class,
        Arguments :
            value : reference to the data the node
            pointer: refrence to the next node
        Return :
            None
    """

    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next


class LinkedList:
    """
    A class for creating instances of a Linked List.

    Fileds :
        No fields

    Behaviours :
        __init__(self):
        The constructor method for the class,
        Arguments :
            self : its the instance we create
        Return :
            None
        add(self,value):
        The Add method for the class,
        Arguments :
            value : data entered at any type
        Return :
            None
    """

    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def contain(self, value):
        while self.head is not None:
            if self.head.value == value:
                return True
            self.head = self.head._next

        return False

    def display(self):
        text=[]
        node = self.head
        while node:
            text+=[str(node.value)]
            node = node._next
        return text


if __name__ == "__main__":

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    print(ll.display())
