def graph_depth_first_search(graph, start_node):
        """
        Traverse a graph in depth first pre-order for a given starting node.

        Argument:
            start_node (vertex): starting node

        Returns:
            list: collection of values in preorder
        """
        visited = []

        def traverse(start_node):
            if start_node in visited:
                return
            visited.append(start_node)
            neighbors = [edge.vertex for edge in graph.get_neighbors(start_node) if edge.vertex not in visited]
            for neighbor in neighbors:
                traverse(neighbor)
        traverse(start_node)
        return [v.value for v in visited]










# def graph_depth_first(graph, start):
#     visited = []
#     stack=[]
#     stack.append(start)
#     visited.append(start)

#     while stack:
#         s=stack.pop()
#         neighbors = graph.get_neighbors(s)
#         for edge in neighbors:
#             neighbor = edge.vertex
#             if neighbor not in visited:
#                 visited.append(neighbor)
#                 stack.append(neighbor)

#     return [vertex.value for vertex in visited]

# def graph_depth_first(graph, start):
#     stack, path = [start], []

#     while stack:
#         vertex = stack.pop()
#         neighbors = [item for item in graph.get_neighbors(vertex)]
#         if vertex in path:
#             continue
#         path.append(vertex)
#         for edge in neighbors:
#             stack.append(edge.vertex)

#     return [vertex.value for vertex in path]

# def graph_depth_first(graph, vertex, path=[]):
#     path += [vertex.value]
#     neighbors = graph.get_neighbors(vertex)

#     for edge in neighbors:
#         neighbor = edge.vertex
#         if neighbor not in path:
#             path = graph_depth_first(graph, neighbor, path)

#     return [vertex for vertex in path]
