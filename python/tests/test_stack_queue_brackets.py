import pytest
from stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_validate_brackets_happy_path():
    actual1 = validate_brackets('{}')
    actual2 = validate_brackets('{}(){}')
    actual3 = validate_brackets('()[[Extra Characters]]')
    actual4 = validate_brackets('{}{Code}[Fellows](())')
    expected = True

    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected
    assert actual4 == expected

def test_validate_brackets_sad_path():
    actual1 = validate_brackets('[({}]')
    actual2 = validate_brackets('(](')
    actual3 = validate_brackets('{(})')
    expected = False

    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected

