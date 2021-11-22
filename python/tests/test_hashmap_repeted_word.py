from hashmap_repeated_word.hashmap_repeated_word import repeated_word

def test_return_repeted_word():
    actual=repeated_word("Once upon a time, there was a brave princess who...")
    excepted="The word is: a"
    assert actual==excepted

def test_return_no_repeted_word():
    actual=repeated_word("String Being passed is empty")
    excepted="No words being catched"
    assert actual==excepted

def test_return_empty_text_passed():
    actual=repeated_word("")
    excepted=('Received error:', 'String Being passed is empty')
    assert actual==excepted
