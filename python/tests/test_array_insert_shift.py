from array_insert_shift.array_insert_shift import insertShiftArray


def test_array_insert():

    actual = insertShiftArray([1, 2], 5)
    accepted = [1, 2, 5]
    assert actual == accepted
