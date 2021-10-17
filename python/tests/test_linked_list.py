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
    expected = 2
    # Actual
    ll = LinkedList()
    actual = ll.add(1)
    actual = ll.add(2)
    actual = ll.head.value
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

def test_linked_str():
    # Arrange
    expected = '{ 3 } -> { 2 } -> { 1 } -> None'
    # Actual
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    actual = str(ll)

    # Assert

    assert expected == actual


def test_linked_list_add_appnd():
    # Arrange
    expected = 2
    # Actual
    ll = LinkedList()
    ll.add_appnd(2)
    actual = ll.head.value
    # Assert
    assert expected == actual


def test_insert_node():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> None'
    # Actual
    ll = LinkedList()
    ll.add_appnd(3)
    ll.add(2)
    ll.add(1)

    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected


def test_insert_multiple_nodes():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 7 } -> { 9 } -> { 11 } -> None'
    # Actual
    ll = LinkedList()
    ll.add_appnd(9)
    ll.add_appnd(11)
    ll.add(7)
    ll.add(2)
    ll.add(1)
    actual = ll.__str__()

    # Assert
    assert actual == expected

def test_insert_node_before_middle():
    # Arrange
    expected = '{ 1 } -> { 4 } -> { 2 } -> { 3 } -> None'
    # Actual
    ll = LinkedList()
    ll.add_appnd(1)
    ll.add_appnd(2)
    ll.add_appnd(3)
    ll.insert_before(2, 4)
    actual = ll.__str__()

    # Assert
    assert actual == expected


def test_insert_node_before_head():
    # Arrange
    expected = '{ 4 } -> { 3 } -> { 2 } -> { 1 } -> None'
    # Actual
    ll = LinkedList()
    ll.add_appnd(4)
    ll.add_appnd(3)
    ll.add_appnd(1)
    ll.insert_before(1, 2)
    actual = ll.__str__()

    # Assert
    assert actual == expected


def test_insert_node_after_middle():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> None'
    # Actual
    ll = LinkedList()
    ll.add_appnd(1)
    ll.add_appnd(2)
    ll.add_appnd(4)
    ll.insert_after(2, 3)
    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected


def test_insert_node_after_end():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> None'
    # Actual
    ll = LinkedList()
    ll.add_appnd(1)
    ll.add_appnd(2)
    ll.add_appnd(3)
    ll.insert_after(3, 4)
    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected
