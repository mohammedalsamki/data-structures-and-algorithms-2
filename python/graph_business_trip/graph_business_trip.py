from graph.graph import *


def business_trip(graph,cities_list):
    if len(cities_list) > 1:
        if not (cities_list[0] in [vertex.value for vertex in graph.get_nodes()]) or  not ( cities_list[1] in [vertex.value for vertex in graph.get_nodes()]):
            return ('NO City')
    vertex_node=graph.get_node(cities_list[0])
    neighbors=graph.get_neighbors(vertex_node)
    if neighbors:
        for neighbor in neighbors:
            if cities_list[1]== neighbor.vertex.value:
                return (True,f'{neighbor.weight}$')
    return(False,'0$')
