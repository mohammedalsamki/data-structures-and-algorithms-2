from stack_and_queue import Stack


class PseudoQueue:

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        The Enqueue Method for Inserts value into the PseudoQueue, using a first-in, first-out approach.
        Arg   : Value with any type
        Return: No return value
        """
        self.stack_1.push(value)
        self.front = self.stack_1.top

    def dequeue(self):
        """
        The Dequeue Method for Extracts a value from the PseudoQueue, using a first-in, first-out approach.h
        Arg   : No Arguments
        Return: value beign removed with any type
        """
        if (self.stack_2.is_empty()):
            while not (self.stack_1.is_empty()):
                self.stack_2.push(self.stack_1.pop())

        return self.stack_2.top.value

    def is_empty(self):
        """
        The Is Empty Method for Check if the Queue is Empty
        Arg   : No Arguments
        Return: True if the Queue is empty and False if Queue is not empty
        """
        return self.stack_1.is_empty() and self.stack_2.is_empty()


if __name__ == "__main__":

    instance = PseudoQueue()
    instance.enqueue(1)
    print(instance.dequeue())
    print(instance.is_empty())
