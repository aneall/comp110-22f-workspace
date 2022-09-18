"""My EX04, where I use list utility functions."""
__author__ = "730604478"


def all(a: list[int], b: int) -> bool:
    # return bool indicating whether or not all the ints in the list are the same as the given int.
    list_length: int = len(a)
    i: int = 0
    if list_length == 0:
        return False
    while i < list_length:
        if a[i] == b:
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    max: int = input[i]
    input_length: int = len(input)
    while i < input_length:
        if max < input[i+1]:
            max = input[i+1]
            i += 1
    return max
        




def is_equal(a: list[int], b: list[int]) -> bool:
    if a == b:
        return True
    else:
        return False
