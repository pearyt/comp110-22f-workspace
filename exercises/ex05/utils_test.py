"""Test for utils."""
__author__ = "730613916"

from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens() -> None:
    """Test two integers."""
    input_list: list[int] = [1, 2]
    assert only_evens(input_list) == [2]    


def test_only_evens_empty() -> None:
    """Test if only odd nums, return empty list."""
    input_list: list[int] = [1]
    assert only_evens(input_list) == []   


def test_only_evens_full() -> None:
    """Test only even nums; should return all values."""
    input_list: list[int] = [4, 4, 4]
    assert only_evens(input_list) == [4, 4, 4]


def test_concat() -> None:
    """Test successive numbers; combine both lists."""
    list_1: list[int] = [1, 2]
    list_2: list[int] = [3, 4]
    assert concat(list_1, list_2) == [1, 2, 3, 4]


def test_empty_list_1() -> None:
    """Test if there an empty list: potential errors?"""
    list_1: list[int] = list()
    list_2: list[int] = [2]
    assert concat(list_1, list_2) == [2]


def test_concat_reverse_order() -> None:
    """Test combining lists to see if they are descending order."""
    list_1: list[int] = [5, 4, 3]
    list_2: list[int] = [2, 1]
    assert concat(list_1, list_2) == [5, 4, 3, 2, 1]


def test_sub_function() -> None:
    """Testing out the sub function."""
    a_list: list[int] = [1, 2, 3, 4]
    start_index: int = 1
    last_index: int = 3
    assert sub(a_list, start_index, last_index) == [2, 3]


def test_sub_negative_start_index() -> None:
    """Test out a negative start index."""
    a_list: list[int] = [1, 2, 3, 4]
    start_index: int = -1
    last_index: int = 2
    assert sub(a_list, start_index, last_index) == [1, 2]


def test_sub_over_index() -> None:
    """Last_index is 0."""
    a_list: list[int] = [1, 2, 3, 4]
    start_index: int = 1
    last_index: int = 0
    assert sub(a_list, start_index, last_index) == []