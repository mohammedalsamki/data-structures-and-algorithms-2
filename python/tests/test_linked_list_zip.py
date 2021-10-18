import tests.linked_list_zip
import pytest

def test_import():
    assert tests.linked_list_zip

def test_linked_list_zipped():
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
    actual = linked_list_zip.zip_list(Linked_List_1,Linked_List_2)
    print(actual)
    # Assert
    assert expected == actual
