"""
The implementation of Node class, Linked list class, and Hashmap class.
"""


import re


class Node:
    def __init__(self, value=None, next_=None):
        """
        Initalization the Node
        """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table

        """
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
      """
      Retrieve the most recent value of in our hasmap for the given key

      Arg: key str
      Return : any
      """

      index = self.__hash(key)

      if self.__buckets[index]:
        linked_list = self.__buckets[index]
        current = linked_list.head
        while current:
          if current.value[0] == key:
            return current.value[1]
          current = current.next

      return None

    def contain(self, key):
        """
        Check if the key exists in the table already.

        Arg: key str
        Return : Boolean
        """

        index = self.__hash(key)
        hashed = self.__buckets[index]
        if hashed:
            current = hashed.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
            return True
        return None

class UnAcceptedValueError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

def repeated_word(text):
    """
    A function finds the first word to occur more than once in a string takes a string, and returns string
    Args : text as string type
    Returns : word as string type
    """
    table = HashTable()
    try:
        words = list(map(lambda word : word.lower(), re.findall(r"\w+", text)))
        if(len(words)==0):
            raise UnAcceptedValueError("String Being passed is empty")
        for word in words:
            if table.contain(word):
                return f"The word is: {word}"
            table.add(word, '.')
    except UnAcceptedValueError as e:
        return("Received error:",e.data)

    else: return "No words being catched"
