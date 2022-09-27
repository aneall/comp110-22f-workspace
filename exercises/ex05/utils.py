"""My utils file within EX05, where I will implement function skeletons."""
__author__ = "730604478"


def only_evens(x: list[int]) -> list:
    """The only_evens function runs through a single given list of integers and returns a new list containing only the even values in the list, in their appearing order."""
    i: int = 0
    evens_list: list = []
    while i < len(x):
        if x[i] % 2 == 0:
            evens_list.append(x[i])
        i += 1
    return evens_list


def concat(x: list[int], y: list[int]) -> list:
    """The concat function runs through two lists; the first list is run through and each value at every index is appended to a new list in their appearing order, followed by all of the values at each index in the second given list; a new list is created from this and returned, showing all values from both lists respectively."""
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
    """The sub function runs through a single given list of integers and uses given 'start' and 'end' integer values to figure out what part of a list (as in, through what range of indices in the given 'x' list) should be returned in a new list."""
    new_list: list = []
    if len(x) == 0 or start > len(x) or end <= 0:
        return new_list
    if start < 0:
        start = 0
    if end > len(x):
        end = len(x)
    while start < end:
        new_list.append(x[start])
        start += 1
    return new_list