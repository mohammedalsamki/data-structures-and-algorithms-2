from collections import deque


class Vertex:
    """
    Class for Adding a node to the graph
    Arguments: value
    Returns: The added node
    """
    def __init__(self,value):
        """
        Initalization for a Vertex to hold a value.
        """
        self.value=value

class Queue:
    """
    Class implementing the double end queue
    for adding the vertices to it
    Arguments : No argumets
    Return : No return
    """
    def __init__(self):
        self.dq=deque()
    """
    Initalization for a Vertex to hold a value.
    """
    def enqueue(self):
        """
        Method to enqueue from deque
        """
        self.dq.appendleft(value)
    def dequeue(self):
        """
        Method to dequeue from deque
        """
        self.dequeue.pop()
    def __len__(self):
        """
        Method to get length of deque
        """
        return len(self.enqueue)

class Stack:
    def __init__(self) -> None:
        """
		Initalization for the stack class with proprites
        of a new double ended que.
	    """
        self.dq=deque()
    def push(self,value):
        """
		Method to store the passed value in a node at the top of stack
        Arguments : value The value that will get stored
        Return : No return
		"""
        self.dq.append(value)
    def pop(self):
        """
		Method to pop from top of stack
        Arguments : No argument
        Return : No return
		"""
        self.dq.pop()
class Edge:
    """
    Class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    """
    def __init__(self,vertex,weight) -> None:
        """
        Initalization for Edge Class with tow proparties
        vertex and weight
        """
        self.vertex=vertex
        self.weight=weight

class Graph:
    def __init__(self):
        """
        Initalization for a hashmap to hold the vertices
        """
        self.__adjacency_list = {}

    def add_node(self,value):
        """
        Method for Adding a node to the graph
        Arguments: value
        Returns: The added node
        """
        v=Vertex(value)
        self.__adjacency_list[v]=[]
        return v
    def add_edge(self,start_vertex,end_vertex,weight=1):
        """
        Method for Adding edge between tow nodes
        Arguments: start_vertex,end_vertex,weight=1
        Returns: No Return value
        """
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")
        edge=Edge(end_vertex,weight)
        self.__adjacency_list[start_vertex].append(edge)
    def size(self):
        """
        Method to size of Graph
        Arguments: None
        return: length of adjeancy
        """
        return len(self.__adjacency_list)

    def get_nodes(self):
        """
        Method to get all nodes in Graph
        Arguments: None
        return: keys of adjency list
        """
        return self.__adjacency_list.keys()
    def get_neighbors(self, vertex):
        """
        Method to get all neighbors in Graph
        Arguments: None
        return: neighbors of vertex in adjency list
        """
        return self.__adjacency_list.get(vertex, [])
    def breadth_first_search(self,start_vertex,end_vertex,action=(lambda vertex:None)):
        queue=Queue()
        visited=set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex=queue.dequeue()
            action(current_vertex)
            neighbors=self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor=edge.vertex

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)



