import pytest
from graph.graph import Graph, Vertex
from graph_business_trip.graph_business_trip import business_trip


def test_business_trip_both_city_not_present():
    graph = Graph()
    path = ['metroville','test']
    excepted = 'NO City'
    actual = business_trip(graph,path)
    assert excepted == actual


def test_business_trip_one_city_not_present():
    graph = Graph()
    graph.add_node('pandora')
    path = ['pandora','test']
    excepted = 'NO City'
    actual = business_trip(graph,path)
    assert excepted == actual


def test_business_trip_cities_dont_have_egde():
    graph = Graph()
    graph.add_node('pandora')
    graph.add_node('Metroville')
    path = ['pandora','Metroville']
    excepted = False,'0$'
    actual = business_trip(graph,path)
    assert excepted == actual

def test_business_trip_cities_do_have_egde():
    graph = Graph()
    pandora = graph.add_node('pandora')
    metroville = graph.add_node('Metroville')
    graph.add_edge(pandora, metroville, 82)
    path = ['pandora','Metroville']
    excepted = True,'82$'
    actual = business_trip(graph,path)
    assert excepted == actual

def test_business_trip_one_city():
    graph = Graph()
    path = ['metroville']
    excepted = False,'0$'
    actual = business_trip(graph,path)
    assert excepted == actual

def test_business_trip_two_paths():
    """
    It should pass if both paths exist with correct weights
    """
    graph = Graph()
    pandora = graph.add_node('pandora')
    metroville = graph.add_node('Metroville')
    arendelle = graph.add_node('arendelle')
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(pandora, arendelle, 150)
    path2 = ['pandora','arendelle']
    path = ['pandora','Metroville']
    excepted = True,'82$'
    excepted2 = True,'150$'
    actual = business_trip(graph,path)
    actual2 = business_trip(graph,path2)
    assert excepted == actual
    assert excepted2 == actual2

def test_business_trip_two_paths_fail():
    graph = Graph()
    pandora = graph.add_node('pandora')
    metroville = graph.add_node('Metroville')
    arendelle = graph.add_node('arendelle')
    naboo = graph.add_node('naboo')
    graph.add_edge(pandora, metroville, 82)
    graph.add_edge(pandora, arendelle, 150)
    path = ['pandora','naboo']
    excepted = False,'0$'
    actual = business_trip(graph,path)
    assert excepted == actual
