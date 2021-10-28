class Node:
    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right

class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

class BinaryTree:
    """
    A binary tree Class

    """

    def __init_(self):
        self.root = None

    def bfs(self):
        """
        A binary tree method which returns a list of items that it contains
        In breadth First Terminology

        Argument: None
        Return: tree items
        """
        breadth = Queue()
        breadth.enqueue(self.root)
        list_of_items = []

        while breadth.peek():
            front = breadth.dequeue()
            list_of_items += [front.value]

            if front.left:
                breadth.enqueue(front.left)

            if front.right:
                breadth.enqueue(front.right)

        return list_of_items

    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains
        In pre Order Terminology

        Argument: None
        Return: tree items
        sub method : traverse to traverse throw the tree
        """
        list_of_items = []

        def traverse(node):
            if node:
                list_of_items.append(node.value)
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)

        traverse(self.root)
        return list_of_items

    def in_order(self):
        """
        A binary tree method which returns a list of items that it contains
        In Order Terminology

        Argument: None
        Return: tree items
        sub method : traverse to traverse throw the tree
        """
        list_of_items = []

        def traverse(node):
            if node:
                if node.left:
                    traverse(node.left)
                list_of_items.append(node.value)
                if node.right:
                    traverse(node.right)

        traverse(self.root)
        return list_of_items

    def post_order(self):
        """
        A binary tree method which returns a list of items that it contains
        In Post Order Terminology

        Argument: None
        Return: tree items
        sub method : traverse to traverse throw the tree
        """
        list_of_items = []

        def traverse(node):
            if node:
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
                list_of_items.append(node.value)

        traverse(self.root)
        return list_of_items
