import pytest

from stack_and_queue import Node
from stack_and_queue import Stack
from stack_and_queue import Queue

def test_stack_push(stack):
    actual = stack.top.value
    expected = 'g'
    assert actual == expected


def test_stack_pop(stack):
    actual = stack.pop()
    excepted = 'g'
    assert actual == excepted


def test_stack_multiple_pop():
    node = Stack()
    node.push('a')
    node.push('b')
    node.push('c')
    node.push('g')
    node.pop()
    node.pop()
    node.pop()
    node.pop()
    actual = node.top
    excepted = None
    assert actual == excepted


def test_stack_peek(stack):
    actual = stack.top.value
    expected = 'g'
    assert actual == expected


def test_stack_peek_next(stack):
    actual = stack.top.next.value
    expected = 'c'
    assert actual == expected


def test_stack_instantiate_empty():
    node = Stack()
    actual = node.top
    excepted = None
    assert actual == excepted


def test_stack_is_empty(stack):
    actual = stack.is_empty()
    excepted = False
    assert actual == excepted


def test_Queue_enqueue(enqueue):
    actual = enqueue.rear.value
    expected = 'g'
    assert actual == expected


def test_Queue_dequeue(enqueue):
    actual = enqueue.dequeue()
    excepted = 'a'
    assert actual == excepted


def test_Queue_multiple_dequeue():
    node = Queue()
    node.enqueue('a')
    node.enqueue('b')
    node.enqueue('c')
    node.enqueue('g')
    node.dequeue()
    node.dequeue()
    node.dequeue()
    node.dequeue()
    actual = node.front
    excepted = None
    assert actual == excepted


def test_Queue_peek(enqueue):
    actual = enqueue.front.value
    expected = 'a'
    assert actual == expected


def test_Queue_peek_next(enqueue):
    actual = enqueue.front.next.value
    expected = 'b'
    assert actual == expected


def test_Queue_instantiate_empty():
    node = Queue()
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
    node = Queue()
    node.enqueue('a')
    node.enqueue('b')
    node.enqueue('c')
    node.enqueue('g')
    return node
