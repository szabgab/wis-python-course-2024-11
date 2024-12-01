from count_digits_in_file import count_digits   

def test_counter():
    res = count_digits("11")
    assert res == [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]

def test_counter2():
    res = count_digits("123")
    assert res == [0, 1, 1, 1, 0, 0, 0, 0, 0, 0]

    