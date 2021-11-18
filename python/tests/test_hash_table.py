from hashtable.hashtable import HashTable
import pytest


def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected

def test_hash_word(hashtable):
	expected = 376
	actual =  hashtable._HashTable__hash("dd")
	assert actual == expected

def test_hash_get(hashtable):
	expected = 22
	actual =  hashtable.get('a')
	assert actual == expected

def test_hash_contain(hashtable):
	expected = True
	actual =  hashtable.contain('a')
	assert actual == expected

def test_hash_not_contain(hashtable):
	expected = None
	actual =  hashtable.contain('k')
	assert actual == expected
    
@pytest.fixture
def hashtable():
    table=HashTable()
    table.add('d',55)
    table.add('a',22)
    return table





