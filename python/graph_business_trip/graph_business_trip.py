from graph.graph import *


def business_trip(graph,trip):
    cost=0
    m={}
    for i in range(len(trip)):
        for city in graph.get_neighbors(trip[0]):
            m[city.vertex.value]=f'{city.weight}'
    if len(m)!=0:
        cost=m.get(trip[1].value)
        return f'There is a Road from {trip[0].value} to {trip[1].value} and it will cost {cost}$'
    else :
        return f'There is No Road'
