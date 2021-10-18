from typing import Text


class Node:
    """
    Class for Node implementation with fields for value and pointer
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

    """

    def __init__(self):
        """
        __init__(self):
        The constructor method for the class,
        Arguments :
            self : its the instance we create
        Return :
            None

        """
        self.head = None

    def add(self, value):
        """
        add(self,value):
        The Add method for the class for adding elmenent to likedlist,
        Arguments :
            value : data entered at any type
        Return :
            None
        """
        new_node = Node(value, self.head)
        self.head = new_node

    def contain(self, value):
        """
        contain(self,value):
        The Contain method for checking if element in linked list,
        Arguments :
            value : data entered at any type
        Return :
            True if element existed
            False if elment is not existed
        """
        while self.head is not None:
            if self.head.value == value:
                return True
            self.head = self.head._next

        return False

    def __str__(self):
        """
        Loop over all the nodes and print all the values in one line
        """
        output = ""
        node = self.head
        while node:
            value = str(node.value)
            if node._next == None:
                output = output + '{ ' + value + ' } -> None'
                break
            else:
                node = node._next
                output = output + '{ ' + value + ' } -> '
        return output


if __name__ == "__main__":

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.display()
