
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
        output = ""
        pointer = self.head
        while pointer:
            if pointer._next is None:
                output += "{ " + f"{str(pointer.value)}" + " }" + " -> None"

            else:
                output += "{ " + f"{str(pointer.value)}" + " }" + " -> "
            pointer = pointer._next
        return output

    def append(self, value='None'):
        """
        Add a node to the end of the linked list
        """
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            pointer = self.head
            while pointer._next is not None:
                pointer = pointer._next
            pointer._next = node

    def insert_before(self, value, new_value):
        """
        adds a new node with the given new value immediately before the first node that has the value specified.
        """
        pointer = self.head
        if pointer.value == value:
            self._next = pointer
            self.head = new_value
        else:
            while pointer:
                if pointer._next.value == value:
                    next_value = pointer._next
                    pointer._next = Node(new_value)
                    pointer._next._next = next_value
                    break
                pointer = pointer._next

    def insert_after(self, value, new_value):
        """
        Adds a new node with new value passed after the first node which has the value specified.
        """
        pointer = self.head
        while pointer:
            if pointer.value == value:
                next_value = pointer._next
                pointer._next = Node(new_value)
                pointer._next._next = next_value
                break
            pointer = pointer._next
            
    def get_k_th(self, k):
        """
        this function return the kth value of list

        Arg:
        k : The nth of the list we need to return and it k is positive integer less
        than the length of linked list

        Return:
        value at kth of linked list
        """
        pointer = self.head
        count = 0
        while (pointer):
            if (count == k):
                return pointer.value
            count += 1
            pointer = pointer._next
        if k == count:
            return "The Length of array and the k you passed are same"
        elif k > count:
            return "You are not allowed to enter a number is greater than length of list"
        elif k < 0:
            return "You are not allowed to enter negative number"
        else:
            return 0


if __name__ == "__main__":

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    print(ll.getNth(2))
    print(ll.__str__())
