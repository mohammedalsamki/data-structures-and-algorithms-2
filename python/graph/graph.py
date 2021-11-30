from collections import deque

class Vertex:
    """
    Class for Adding a node to the graph
    Arguments: value
    Returns: The added node
    """
    def __init__(self, value):
        """
        Initalization for a Vertex to hold a value.
        """
        self.value = value

class Queue:
    """
    Class implementing the double end queue
    for adding the vertices to it
    Arguments : No argumets
    Return : No return
    """
    def __init__(self):
        """
        Initalization for a Vertex to hold a value.
        """
        self.dq = deque()

    def enqueue(self, value):
        """
        Method to enqueue from deque
        """
        self.dq.appendleft(value)

    def dequeue(self):
        """
        Method to dequeue from deque
        """
        return self.dq.pop()

    def __len__(self):
        """
        Method to get length of deque
        """
        return len(self.dq)

class Stack:
    """
    A data structure that utilitzes the first in last out access method.
    """
    def __init__(self):
        """
		The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
		"""
        self.dq = deque()

    def push(self, value):
        """
        Push a value in a node on top of a stack.
        Args:
            value (any): The value to be pushed on top of the stack.
        """
        self.dq.append(value)

    def pop(self):
        """
        Pop or get the very last item in a stack.
        """
        self.dq.pop()

class Edge:
    """
    Class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    """
    def __init__(self, vertex, weight):
        """
        Initalization for Edge Class with tow proparties
        vertex and weight
        """
        self.vertex = vertex
        self.weight = weight

class Graph:
    """
    Initalization for a hashmap to hold the vertices
    """
    def __init__(self):
        """
        A constructor method of the class Graph. Initialize the adjacency_list property.
        """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
        Method for Adding a node to the graph
        Arguments: value
        Returns: The added node
        """
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def get_node(self,value):
        nodes=[]
        for node in list(self.get_nodes()):
            nodes+=[node.value]
            if value in nodes:
                return node

    def size(self):
        """
        Get the number of vertices in a graph.
        Returns:
            int: The number of nodes or vertices in a graph.
        """
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=1):
        """
        Method for Adding edge between tow nodes
        Arguments: start_vertex,end_vertex,weight=1
        Returns: No Return value
        """
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
        Return all the nodes in a graph.
        Returns:
            list: A list of all the vertices in a graph.
        """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        Method to get all neighbors in Graph
        Arguments: None
        return: neighbors of vertex in adjency list
        """
        return self.__adjacency_list.get(vertex, [])

    def breadth_first_search(self, start_vertex):
        """
        Traverse a graph in breadth first search manner.
        Args:
            start_vertex (vertex): the vertex to start traversing from.
            action (function, optional): the action we want to execute or apply on each vertex in a graph. Defaults to (lambda vertex: None).
        """
        queue = Queue()
        visited = set()
        nodes = []

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            nodes.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        return neighbors
