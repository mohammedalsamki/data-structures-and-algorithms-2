from linked_list import Node, LinkedList
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

def test_linked_list_str():
    # Arrange
    expected = '{ 1 } -> None'
    # Actual
    ll = LinkedList()
    ll.add(1)
    actual = ll.__str__()
    print(actual)
    # Assert

    assert expected == actual

# @pytest.mark.skip()
def test_linked_list_append():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> None'
    # Actual
    ll = LinkedList()
    ll.add(1)
    ll.append(2)
    ll.append(3)
    actual = ll.__str__()
    print(actual)
    # Assert
    assert expected == actual

# @pytest.mark.skip()
def test_linked_list_insert_before():
    # Arrange
    expected = '{ 2 } -> { 3 } -> { 1 } -> None'
    # Actual
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.insert_before(1,3)

    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected

# @pytest.mark.skip()
def test_insert_before_multiple_nodes():
    # Arrange
    expected = '{ 1 } -> { 7 } -> { 2 } -> { 5 } -> { 3 } -> None'
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(3,5)
    ll.insert_before(2,7)

    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected
# @pytest.mark.skip()
def test_insert_node_before_middle():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> None'
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.append(5)
    ll.insert_before(4, 3)
    actual = ll.__str__()

    # Assert
    assert actual == expected



# @pytest.mark.skip()
def test_insert_node_after_middle():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> None'
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.insert_after(2, 3)
    ll.append(4)

    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected


# @pytest.mark.skip()
def test_insert_node_after_end():
    # Arrange
    expected = '{ 3 } -> { 2 } -> { 1 } -> { 0 } -> None'
    # Actual
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.append(0)
    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected

# @pytest.mark.skip()
def test_get_k_th():
    # Arrange
    expected = 3
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.get_k_th(2)
    print(actual)
    # Assert
    assert actual == expected

def test_get_k_th_if_number_passed_greater_than_length_of_list():
    # Arrange
    expected = "You are not allowed to enter a number is greater than length of list"
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.get_k_th(5)
    print(actual)
    # Assert
    assert actual == expected


def test_get_k_th_if_number_passed_is_negative():
    # Arrange
    expected = "You are not allowed to enter negative number"
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.get_k_th(-1)
    print(actual)
    # Assert
    assert actual == expected

def test_get_k_th_if_list_length_is_unity():
    # Arrange
    expected = 1
    # Actual
    ll = LinkedList()
    ll.append(1)
    actual = ll.get_k_th(0)
    print(actual)
    # Assert
    assert actual == expected
def test_get_k_th_if_list_in_the_middle():
    # Arrange
    # '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> None' expected
    expected = 3
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.append(5)
    ll.insert_before(4, 3)
    actual = ll.get_k_th(2)

    # Assert
    assert actual == expected

def test_get_k_if_the_k_and_length_are_same():
    # Arrange
    # expected '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> None'
    expected = "The Length of array and the k you passed are same"
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.append(5)
    ll.insert_before(4, 3)
    actual = ll.get_k_th(5)

    # Assert
    assert actual == expected

