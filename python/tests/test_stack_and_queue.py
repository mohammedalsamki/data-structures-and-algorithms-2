import pytest
from stack_and_queue.stack_and_queue import Stack
from stack_and_queue.stack_and_queue import Node
import sys
sys.path.append(
    '/media/jehadabuawwad/EA20F40B20F3DC8F/data-structures-and-algorithms/python')


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
    node=Stack()
    actual = node.top
    excepted = None
    assert actual == excepted

def test_stack_is_empty(stack):
    actual = stack.is_empty()
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
