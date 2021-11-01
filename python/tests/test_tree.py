"""
Binary Tree Tests
"""

from trees.tree import BinaryTree, Node, BinarySearchTree
import pytest

def test_breadth_first(tree_builder):
    expected = ["A", "B", "C", "D"]
    actual = tree_builder.breadth_first()
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

def test_bst_root_addition():
    bst = BinarySearchTree()
    bst.add("X")
    expected = "X"
    actual = bst.root.value
    assert actual == expected

def test_bst_mulitple_values_addition(addition):
    assert addition.root.value == 22
    assert addition.root.right.value == 55
    assert addition.root.left.value == 10

def test_bst_four_values_addition(addition):
    assert addition.root.value == 22
    assert addition.root.right.value == 55
    assert addition.root.left.value == 10
    assert addition.root.left.right.value == 11

def test_bst_find_Max(build_tree_for_max):
    actual=build_tree_for_max.findMax(build_tree_for_max.root)
    expected=11
    assert actual==expected

@pytest.fixture
def addition():
    breadth_first = BinarySearchTree()
    breadth_first.add(22)
    breadth_first.add(10)
    breadth_first.add(55)
    breadth_first.add(11)
    return breadth_first

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

@pytest.fixture
def build_tree_for_max():
    tree = BinaryTree()
    a_node = Node(2)
    b_node = Node(7)
    c_node = Node(5)
    d_node = Node(2)
    e_node = Node(6)
    f_node = Node(9)
    g_node = Node(4)
    h_node = Node(11)
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    c_node.right = f_node
    e_node.left = f_node
    e_node.right = h_node
    f_node.left = g_node
    tree.root = a_node
    return tree

