from graph.graph import *
from graph_depth_first.graph_depth_first import graph_depth_first_search
import pytest

def test_pass(graph_maker):
    graph,a,b,c=graph_maker
    actual1 = graph_depth_first_search(graph,a)
    actual2 = graph_depth_first_search(graph,b)
    actual3 = graph_depth_first_search(graph,c)
    assert actual1== ['a', 'b', 'd', 'f', 'h', 'e', 'c', 'g']
    assert actual2==['b', 'a', 'd', 'f', 'h', 'e', 'c', 'g']
    assert actual3==['c', 'b', 'a', 'd', 'f', 'h', 'e', 'g']


@pytest.fixture

def graph_maker():
    graph=Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    e = graph.add_node("e")
    f = graph.add_node("f")
    g = graph.add_node("g")
    h = graph.add_node("h")

    graph.add_edge(a, b)
    graph.add_edge(a, d)
    graph.add_edge(b, a)
    graph.add_edge(b, d)
    graph.add_edge(b, c)
    graph.add_edge(c, b)
    graph.add_edge(c, g)
    graph.add_edge(d, a)
    graph.add_edge(d, b)
    graph.add_edge(d, f)
    graph.add_edge(d, h)
    graph.add_edge(d, e)
    graph.add_edge(e, d)
    graph.add_edge(f, d)
    graph.add_edge(f, h)
    graph.add_edge(g, c)
    graph.add_edge(h, d)
    graph.add_edge(h, f)

    return graph,a,b,c

