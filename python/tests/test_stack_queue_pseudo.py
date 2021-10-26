import pytest

from stack_and_queue.stack_and_queue import Node
from stack_and_queue.stack_and_queue import Stack
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue


def test_Queue_enqueue(enqueue):
    actual = enqueue.front.value
    expected = 'g'
    assert actual == expected


def test_Queue_dequeue(enqueue):
    actual = enqueue.dequeue()
    excepted = 'a'
    assert actual == excepted


def test_Queue_multiple_dequeue():
    node = PseudoQueue()
    node.enqueue('a')
    node.enqueue('b')
    node.enqueue('c')
    node.enqueue('g')
    node.dequeue()
    node.dequeue()
    node.dequeue()
    actual = node.stack_2.pop()
    excepted = 'a'
    assert actual == excepted


def test_Queue_peek(enqueue):
    actual = enqueue.front.value
    expected = 'g'
    assert actual == expected


def test_Queue_peek_next(enqueue):
    actual = enqueue.front.next.value
    expected = 'c'
    assert actual == expected


def test_Queue_instantiate_empty():
    node = PseudoQueue()
    actual = node.front
    excepted = None
    assert actual == excepted


def test_Queue_is_empty(enqueue):
    actual = enqueue.is_empty()
    excepted = False
    assert actual == excepted


@pytest.fixture
def stack():
    node = Stack()
    node.push('a')
    node.push('b')
    node.push('c')
    node.push('g')
    return node


@pytest.fixture
def enqueue():
    node = PseudoQueue()
    node.enqueue('a')
    node.enqueue('b')
    node.enqueue('c')
    node.enqueue('g')
    return node
