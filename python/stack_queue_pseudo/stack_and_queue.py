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
        The Is Empty Method for Check if the Stack is Empty
        Arg   : No Arguments
        Return: True if the stack is empty and False if stack is not empty
        """
        return not self.top


class Queue(Node):
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        The Enqueue Method for adding value to the rear of Queue
        Arg   : Value with any type
        Return: No return value
        """
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        The Dequeue Method for removing value from front of the Queue
        Arg   : No Arguments
        Return: value beign removed with any type
        """
        if self.front == None:
            raise Exception("This stack is empty")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        """
        The Peek Method for showing to front value in the Queue
        Arg   : No Arguments
        Return: value at the front of Queue with any type
        """
        return self.front.value

    def is_empty(self):
        """
        The Is Empty Method for Check if the Queue is Empty
        Arg   : No Arguments
        Return: True if the Queue is empty and False if Queue is not empty
        """
        return not self.front
