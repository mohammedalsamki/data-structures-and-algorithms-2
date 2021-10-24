from linked_list_zip import *
from linked_list import Node, LinkedList

import pytest


def test_linked_list_zipped_after_add():
    # Arrange
    expected = 'head -> { 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> X'
    # Actual
    Linked_List_1=LinkedList()
    Linked_List_2=LinkedList()

    Linked_List_1.add(1)
    Linked_List_1.add(3)
    Linked_List_1.add(2)
    Linked_List_2.add(5)
    Linked_List_2.add(9)
    Linked_List_2.add(4)
    actual = zip_list(Linked_List_1,Linked_List_2)
    print(actual)
    # Assert
    assert expected == actual

def test_linked_list_zipped_after_append():
    # Arrange
    expected = 'head -> { 2 } -> { 4 } -> { 3 } -> { 9 } -> { 1 } -> { 5 } -> X'
    # Actual
    Linked_List_1=LinkedList()
    Linked_List_2=LinkedList()

    Linked_List_1.append(1)
    Linked_List_1.append(3)
    Linked_List_1.append(2)
    Linked_List_2.append(5)
    Linked_List_2.append(9)
    Linked_List_2.append(4)
    actual = zip_list(Linked_List_1,Linked_List_2)
    print(actual)
    # Assert
    assert expected == actual

def test_linked_list_zipped_with_after():
    # Arrange
    expected = 'head -> { 8 } -> { 7 } -> { 1 } -> { 3 } -> { 5 } -> { 8 } -> X'
    # Actual
    Linked_List_1=LinkedList()
    Linked_List_2=LinkedList()

    Linked_List_1.add(1)
    Linked_List_2.add(7)

    Linked_List_1.insert_after(1,8)
    Linked_List_2.add(3)

    Linked_List_1.add(5)
    Linked_List_2.add(8)

    actual = zip_list(Linked_List_1,Linked_List_2)
    print(actual)
    # Assert
    assert expected == actual

