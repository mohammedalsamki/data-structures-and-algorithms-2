
from graph.graph import *
from graph_business_trip.graph_business_trip import business_trip

def test_business_trip_path_1():
    graph=Graph()
    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    narina = graph.add_node('narina')
    naboo = graph.add_node('naboo')
    manstropolis = graph.add_node('manstropolis')
    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(narina, metroville, 37)
    graph.add_edge(naboo, narina, 250)
    graph.add_edge(naboo, manstropolis, 73)
    graph.add_edge(manstropolis, arendelle, 42)
    graph.add_edge(manstropolis, metroville, 105)

    distinations=[pandora,metroville]
    actual=business_trip(graph,distinations)
    print(actual)
    expected='There is a Road from pandora to metroville and it will cost 82$'
    assert actual==expected


def test_business_trip_path_2():
    graph=Graph()
    pandora = graph.add_node('pandora')
    arendelle = graph.add_node('arendelle')
    metroville = graph.add_node('metroville')
    narina = graph.add_node('narina')
    naboo = graph.add_node('naboo')
    manstropolis = graph.add_node('manstropolis')
    graph.add_edge(pandora, arendelle, 150)
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(arendelle, metroville, 99)
    graph.add_edge(metroville, naboo, 26)
    graph.add_edge(narina, metroville, 37)
    graph.add_edge(naboo, narina, 250)
    graph.add_edge(naboo, manstropolis, 73)
    graph.add_edge(manstropolis, arendelle, 42)
    graph.add_edge(manstropolis, metroville, 105)

    distinations=[pandora,naboo]
    actual=business_trip(graph,distinations)
    print(actual)
    expected='There is No Road'
    assert actual==expected








# @pytest.fixture

# def GraphBuilder():


#     return graph,pandora,arendelle,metroville,narina,naboo,manstropolis
