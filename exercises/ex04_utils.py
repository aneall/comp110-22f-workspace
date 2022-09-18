"""My EX04, where I use list utility functions."""
__author__ = "730604478"


def all(a: list[int], b: int) -> bool:  # All returns a bool, indicating if all the ints in the list are the same as the given int or not.
    """The all function checks to see if a list passed to it only contains the same integer, and if that integer is the same as the integer passed to it."""
    list_length: int = len(a)
    i: int = 0
    if list_length == 0:  # here we first designate that if the length of list a is 0 (aka it's an empty list), then we will immediately return false because we can't compare the list values to the integer if there are no list values.
        return False
    while i < list_length:  # in this loop, we first make sure that the current index is less than the length of list a since i begins at 0 
        if a[i] == b:  # ^^^ then we check to see if the number at a certain index in list a is equal to that in list b; if so, we add to 1; if they are not equal at any point, we must return false and exit the function.
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:  # retruns an int, indicating what the maximum value is in a given list.
    """The max function checks to see what the maximum integer value is in a list passed to it."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    max_nbr: int = input[i]
    input_length: int = len(input)
    while i < (input_length - 1):  # in this loop, we compare the current max number to the next number in the list.
        if max_nbr < input[i + 1]:  # if the next number is greater than the current max number, it becomes the new max number; this continues until we find the highest value number.
            max_nbr = input[i + 1]
        i += 1
    return max_nbr


def is_equal(a: list[int], b: list[int]) -> bool:  # returns a bool, indicating if the first given list of integers is equal to the other given list of integers.
    """The is_equal function checks to see if two lists passed to it are equal to each other."""
    if a == b:  # in this if-else statement, we indicate if the list a is equal to list b; if so, we return true; if not, we return false.
        return True
    else:
        return False
