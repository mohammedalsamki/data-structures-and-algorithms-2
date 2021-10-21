class Node:
    """
    The Node class which will be a part of stack
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack(Node):
    """
    The Stack class which will have the top field
    """
    def __init__(self, top=None):
        self.top = top
    def push(self, value):
        """
        The Push Method for adding value to the stack
        Arg   : Value with any type
        Return: No return value
        """
        node = Node(value)
        node.next = self.top
        self.top = node
    def pop(self):
        """
        The Pop Method for removing value to the stack
        Arg   : No Arguments
        Return: value beign removed with any type
        """
        if self.top == None:
            raise Exception("This stack is empty")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value
    def peek(self):
        """
        The Peek Method for showing to top value in the stack
        Arg   : No Arguments
        Return: value at the top of stack with any type
        """
        return self.top.value
    def is_empty(self):
        """
        The Is Empty Method for showing to top value in the stack
        Arg   : No Arguments
        Return: True if the stack is empty and False if stack is not empty
        """
        return not self.top
