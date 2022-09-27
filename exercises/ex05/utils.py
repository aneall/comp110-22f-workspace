"""My utils file within EX05, where I will implement function skeletons."""
__author__ = "730604478"


def only_evens(x: list[int]) -> list:
    i: int = 0
    evens_list: list = []
    while i < len(x):
        if x[i] % 2 == 0:
            evens_list.append(x[i])
        i += 1
    return evens_list



def concat(x: list[int], y: list[int]) -> list:
    i: int = 0
    new_list: list = []
    while i < len(x):
        new_list.append(x[i])
        i += 1
    i = 0
    while i < len(y):
        new_list.append(y[i])
        i += 1
    return new_list




def sub(x: list[int], start: int, end: int) -> list:
    new_list: list = []
    if len(x) == 0:
        start > len(x) or end <= 0
        return new_list
    if start < 0:
        start = 0
    if end > len(x):
        end = len(x) - 1
    while start < end:
        new_list.append(x[start])
        start += 1
    return new_list