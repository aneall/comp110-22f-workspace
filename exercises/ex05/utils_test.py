"""My utils testing file within EX05, where I will define at least 3 unit tests for each of the 3 functions."""
__author__ = "730604478"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """A test for the only_evens function to make sure that when an empty list is used as the parameter, an empty list is returned since there are no even values."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_two_evens() -> None:
    """A test for the only_evens function to make sure that when a list with length of 6 with 3 even values is used as the parameter, a list of 3 even values is returned since 4 and 6 are even."""
    x: list[int] = [4, 1, 3, 6, 4, 7]
    assert only_evens(x) == [4, 6, 4]


def test_only_evens_no_evens() -> None:
    """A test for the only_evens function to make sure that when a list with length of 4 that contains only odd values is used as the parameter, a an empty list is eturned since no values are even."""
    x: list[int] = [1, 7, 11, 5]
    assert only_evens(x) == []


def test_only_evens_all_evens() -> None:
    """A test for the only_evens function to make sure that when a list with length 4 that contains only even values is used as the parameter, a list of the same 4 even values is returned since all the values are even."""
    x: list[int] = [2, 6, 16, 8]
    assert only_evens(x) == [2, 6, 16, 8]


def test_concat_one_empty_list() -> None:
    """A test for the concat function to make sure that when one list with length 3 and another empty list are used as the parameters, a list identical to the first list is returned."""
    x: list[int] = [1, 2, 3]
    y: list[int] = []
    assert concat(x, y) == [1, 2, 3]


def test_concat_use_case() -> None:
    """A test for the concat function to make sure that when one list with length 3 and another list with length 2 are used as the parameters, a list that appends the latter onto the first list is first list is correctly returned."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [1, 2]
    assert concat(x, y) == [1, 2, 3, 1, 2]


def test_concat_another_use_case() -> None:
    """A test for the concat function to make sure that when one list with length 2 (that has the same values in both indices) and another list with length 2 are used as the parameters, a list that begins with the first list and appends the second list is returned."""
    x: list[int] = [4, 4]
    y: list[int] = [3, 4]
    assert concat(x, y) == [4, 4, 3, 4]


def test_concat_two_empty_lists() -> None:
    """A test for the concat function to make sure that when two empty lists are used as the parameters, an empty list is returned."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_sub_negative_end() -> None:
    """A test for the sub function to make sure that when the 'end' parameter is less than 0, an empty list is returned."""
    x: list[int] = [1, 2, 3]
    start: int = 2
    end: int = -1
    assert sub(x, start, end) == []


def test_sub_start_too_big() -> None:
    """A test for the sub function to make sure that when the 'start' parameter is greater than the length of the list, an empty list is returned."""
    x: list[int] = [1, 2, 3]
    start: int = 5
    end: int = 4
    assert sub(x, start, end) == []


def test_sub_first_two_indices() -> None:
    """A test for the sub function to make sure that when the 'x' parameter is a list of length 4, 'start' is 0, and 'end' is 2, a list that only mentions the 0th through 1st index is returned."""
    x: list[int] = [20, 50, 30, 60]
    start: int = 0
    end: int = 2
    assert sub(x, start, end) == [20, 50]


def test_sub_another_use() -> None:
    """A test for the sub function to make sure that when the 'x' parameter is a list of length 5, 'start' is 1, and 'end' is 4, a list that only mentions the 1st through 3rd index is returned."""
    x: list[int] = [3, 18, 6, 3, 5]
    start: int = 1
    end: int = 4
    assert sub(x, start, end) == [18, 6, 3]