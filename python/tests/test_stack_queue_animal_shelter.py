import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter

def test_add_animal():
    shelt = AnimalShelter()
    shelt.add_animal("suzy","cat")
    shelt.add_animal("razan","cat")
    shelt.add_animal("razan","cat")

    actual = shelt.rear.value
    expected = {'name': 'razan', 'type': 'cat'}
    print(actual)
    assert actual == expected


def test_adopt_animal():
    shelt = AnimalShelter()
    shelt.add_animal("sobhi","dog")
    shelt.add_animal("hassona","dog")
    shelt.adopt_animal("dog")

    actual = shelt.front.value
    excepted = {'name': 'hassona', 'type': 'dog'}
    assert actual == excepted

def test_Queue_is_empty():
    shelt = AnimalShelter()
    shelt.add_animal("sobhi","dog")
    shelt.adopt_animal("dog")
    actual=shelt.front
    excepted = None
    assert actual == excepted


