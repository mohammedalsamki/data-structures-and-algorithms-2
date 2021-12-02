
import pytest
from hashmap_left_join.dependices import *
from hashmap_left_join.hash_map_left_join import left_join

def test_same_keys():
    """
    The keys are the same and the values are different
    """
    left_hash_map = HashTable()
    right_hash_map = HashTable()
    left_values = [("a", "A"), ("b", "B"),("c","C"),]
    right_values = [("a","X"),("b","Y"),("c", "Z"),]
    for key, value in left_values:
        left_hash_map.add(key, value)
    for key, value in right_values:
        right_hash_map.add(key, value)
    actual=left_join(left_hash_map, right_hash_map)
    expected = [('a', ('A', 'X')), ('b', ('B', 'Y')), ('c', ('C', 'Z'))]
    print(actual)
    assert  actual== expected

def test_same_keys_in_one_hash_map():
    """
    One hash map all keys of it are the same
    """
    left_hash_map = HashTable()
    right_hash_map = HashTable()
    left_values = [("a", "a"), ("b", "b"),("c","c"),]
    right_values = [("a","1"),("a","2"),("a", "3"),]
    for key, value in left_values:
        left_hash_map.add(key, value)
    for key, value in right_values:
        right_hash_map.add(key, value)
    actual=left_join(left_hash_map, right_hash_map)
    expected = [('a', ('a', '3')), ('a', ('a', '2')), ('a', ('a', '1')), ('b', ('b', None)), ('c', ('c', None))]
    print(actual)
    assert  actual== expected

def test_different_keys():
    """
    The keys are different for both hashmaps
    """
    left_hash_map = HashTable()
    right_hash_map = HashTable()
    left_values = [("a", "a"), ("b", "b"),("c","c"),]
    right_values = [("i","1"),("j","2"),("k", "1"),]
    for key, value in left_values:
        left_hash_map.add(key, value)
    for key, value in right_values:
        right_hash_map.add(key, value)
    actual=left_join(left_hash_map, right_hash_map)
    expected = [('a', ('a', None)), ('b', ('b', None)), ('c', ('c', None))]
    print(actual)
    assert  actual== expected

def test_empty_hash_map():
    """
    One hash map is empty
    """
    left_hash_map = HashTable()
    right_hash_map = HashTable()
    left_values = []
    right_values = [("a","X"),("b","Y"),("c", "Z"),]
    for key, value in left_values:
        left_hash_map.add(key, value)
    for key, value in right_values:
        right_hash_map.add(key, value)
    actual=left_join(left_hash_map, right_hash_map)
    expected = []
    assert  actual== expected


