from sorted_join import sorted_join

def test_sorted_join_1():
    assert sorted_join([[1, 2, 7, 9], [3, 6, 8]]) == [1, 2, 3, 6, 7, 8, 9], "Should be [1, 2, 3, 6, 7, 8, 9]"


def test_sorted_join_2():
    assert sorted_join([[6, 8, 9], [1, 4, 6]]) == [1, 4, 6, 6, 8, 9], "Should be [1, 4, 6, 6, 8, 9]"


def test_sorted_join_3():
    assert sorted_join([[], [1, 2, 3]]) == [1, 2, 3], "Should be [1, 2, 3]"