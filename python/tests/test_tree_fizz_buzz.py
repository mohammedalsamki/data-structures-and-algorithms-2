"""
K-ary Tree Fizz Buzz Tests
"""
from trees.tree import Queue,kArrayTree,Node
from tree_fizz_buzz.tree_fizz_buzz import *
import pytest

def test_breadth_first(tree_builder):
    expected = [1, 3, 5, 2, 4, 6, 11, 15]
    actual = tree_builder.breadth_first()
    assert actual == expected

def test_empty_breadth_first(tree_builder):
    tree=kArrayTree()
    tree=tree.breadth_first()
    expected = None
    actual = fizz_buzz_tree(tree)
    assert actual == expected

def test_fizz_buzz_tree(tree_builder):
    tree=tree_builder
    tree=tree.breadth_first()
    expected = ['1', 'Fizz', 'Buzz', '2', '4', 'Fizz', '11', 'FizzBuzz']
    actual = fizz_buzz_tree(tree)
    assert actual == expected


@pytest.fixture
def tree_builder():
    a=1
    b=3
    c=5
    d=2
    e=4
    f=6
    g=11
    h=15

    nod_a=Node(a)
    nod_c=Node(c)
    nod_b=Node(b)
    nod_d=Node(d)
    nod_e=Node(e)
    nod_f=Node(f)
    nod_g=Node(g)
    nod_h=Node(h)

    nod_a.add_child(nod_b)
    nod_a.add_child(nod_c)
    nod_a.add_child(nod_d)
    nod_a.add_child(nod_e)
    nod_a.add_child(nod_f)
    nod_a.add_child(nod_g)
    nod_a.add_child(nod_h)

    tree=kArrayTree()
    tree.root = nod_a

    return tree
