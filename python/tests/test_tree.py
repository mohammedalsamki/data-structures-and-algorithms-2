"""
Binary Tree Tests
"""

from trees.tree import BinaryTree, Node
import pytest


def test_bfs(tree_builder):
    expected = ["A", "B", "C", "D"]
    actual = tree_builder.bfs()
    assert actual == expected

def test_pre_order(tree_builder):
    expected = ["A", "B", "D", "C"]
    actual = tree_builder.pre_order()
    assert actual == expected

def test_post_order(tree_builder):
    expected = ["D", "B", "C", "A"]
    actual = tree_builder.post_order()
    assert actual == expected

def test_in_order(tree_builder):
    expected = ["D", "B", "A", "C"]
    actual = tree_builder.in_order()
    assert actual == expected

@pytest.fixture
def tree_builder():
    tree = BinaryTree()
    a_node = Node("A")
    b_node = Node("B")
    c_node = Node("C")
    d_node = Node("D")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    tree.root = a_node

    return tree
