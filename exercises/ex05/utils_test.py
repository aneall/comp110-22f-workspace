"""My utils testing file within EX05, where I will define at least 3 unit tests for each of the 3 functions."""
__author__ = "730604478"


from exercises.ex05.utils import only_evens,concat,sub


def test_only_evens_empty() -> None:
    x: list[int] = []
    assert only_evens(x) == []

def test_only_evens_two_evens() -> None:
    x: list[int] = [4,1,3,6,4,7]
    assert only_evens(x) == [4,6,4]

def test_only_evens_no_evens() -> None:
    x: list[int] = [1,7,11,5]
    assert only_evens(x) == []

def test_only_evens_all_evens() -> None:
    x: list[int] = [2,6,16,8]
    assert only_evens(x) == [2,6,16,8]




def test_concat_one_empty_list() -> None:
    x: list[int] = [1,2,3]
    y: list[int] = []
    assert concat(x,y) == [1,2,3]

def test_concat_use_case() -> None:
    x: list[int] = [1,2,3]
    y: list[int] = [1,2]
    assert concat(x,y) == [1,2,3,1,2]

def test_concat_another_use_case() -> None:
    x: list[int] = [4,4]
    y: list[int] = [3,4]
    assert concat(x,y) == [4,4,3,4]

def test_concat_two_empty_lists() -> None:
    x: list[int] = []
    y: list[int] = []
    assert concat(x,y) == []



def sub_negative_end() -> None:
    x: list[int] = [1,2,3]
    start: int = 2
    end: int = -1
    assert sub(x,start,end) == []

def sub_start_too_big() -> None:
    x: list[int] = [1,2,3]
    start: int = 5
    end: int = 3
    assert sub(x,start,end) == []

def sub_first_two_indices() -> None:
    x: list[int] = [20,50,30,60]
    start: int = 0
    end: int = 2
    assert sub(x,start,end) == [20,50]

def sub_another_use() -> None:
    x: list[int] = [3,18,6,3,5]
    start: int = 1
    end: int = 4
    assert sub(x,start,end) == [18,6,3]