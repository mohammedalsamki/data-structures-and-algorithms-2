import pytest
from tree_intersection.dependices import BinarySearchTree
from tree_intersection.tree_intersection import tree_intersection


def test_tree_intersection():
    a = BinarySearchTree(*[1,2,1])
    b = BinarySearchTree(*[1,2,3])
    assert tree_intersection(a,b) == [1,2]


def test__no_tree_intersection():
    a = BinarySearchTree([2])
    b = BinarySearchTree([1,3])
    assert tree_intersection(a,b) == None

def test_one_empty_tree_intersection():
    a = BinarySearchTree([])
    b = BinarySearchTree([1])
    assert tree_intersection(a,b) == None

@pytest.mark.parametrize(
    "tree_a,tree_b,intersections",
    [
        ([5,6,7], [5,6,7], (5,6,7)),
        ([8], [1,3],None ),
        ([1,5], [1,5], (1,5)),
        ([1],[2],None),
    ]
)
def test_tree_intersection(tree_a, tree_b, intersections):
    a = BinarySearchTree(*tree_a)
    b = BinarySearchTree(*tree_b)
    assert tree_intersection(a,b) == intersections
