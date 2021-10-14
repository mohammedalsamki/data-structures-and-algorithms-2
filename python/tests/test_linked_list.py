from linked_list.linked_list import Node, LinkedList
import pytest


def test_import():
    assert LinkedList


def test_node_is_a_Node():
    # Arrange
    expected = "Node"

    # Actual
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected


def test_node_without_value():
    with pytest.raises(TypeError):
        node = Node()


def test_new_linked_list_is_empty():
    # Arrange
    expected = None
    # Actual
    ll = LinkedList()
    actual = ll.head
    # Assert
    assert actual == expected


def test_node_has_int_data():
    # Arrange
    expected = 1

    # Actual
    node = Node(1)
    actual = node.value

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange
    expected = "a"

    # Actual
    node = Node("a")
    actual = node.value

    # Assert
    assert actual == expected


def test_linked_list_add():
    # Arrange
    expected = None
    # Actual
    ll = LinkedList()
    actual = ll.add(1)
    actual = ll.add(12)
    # Assert
    assert expected == actual


def test_linked_list_contatin():
    # Arrange
    expected = True
    # Actual
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    actual = ll.contain(1)

    # Assert

    assert expected == actual

def test_linked_display():
    # Arrange
    expected = ['2','1']
    # Actual
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    actual = ll.display()

    # Assert

    assert expected == actual
