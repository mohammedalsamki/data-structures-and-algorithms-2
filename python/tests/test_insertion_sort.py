from insertion_sort.insertion_sort import insertion_sort
import pytest


def test_linked_list_insertion_sort_sample():
    expected =  [4, 8, 15, 16, 23, 42]
    actual =insertion_sort([8,4,23,42,16,15])
    assert expected == actual

def test_linked_list_insertion_sort_reverse_sorted():
    expected =  [-2, 5, 8, 12, 18, 20]
    actual =insertion_sort([20,18,12,8,5,-2])
    assert expected == actual

def test_linked_list_insertion_sort_few_uniques():
    expected =  [5, 5, 5, 7, 7, 12]
    actual =insertion_sort([5,12,7,5,5,7])
    assert expected == actual

def test_linked_list_insertion_sort_nearly_sorted():
    expected =  [2, 3, 5, 7, 11, 13]
    actual =insertion_sort([2,3,5,7,13,11])
    assert expected == actual
