"""A program for doing unit testing with dictionaries; at least 3 unit tests for each function."""
__author__ = "730604478"

from exercises.ex07.dictionary import invert, favorite_color, count

import pytest


def test_invert_all_same() -> None:
    """A test to see if an error results when all pairs are the same."""
    with pytest.raises(KeyError):
        my_dictionary = {"a": "hello", "a": "hello", "a": "hello"}
        invert(my_dictionary)

def test_invert_three_elements() -> None:
    """A test to see that if three pairs are entered as our argument, it will result in three inverted pairs."""
    assert invert({"a": "1", "b": "2", "c": "3"}) == {"1": "a", "2": "b", "3": "c"}

def test_invert_one_elements() -> None:
    """A test to see that if one pair is entered as our argument, it will result in one inverted pair."""
    assert invert({"a": "5"}) == {"5": "a"}


def test_only_one_favorite_color() -> None:
    """A test to see if when only one color is in the argument, it returns that color as the favorite."""
    assert favorite_color({"Ashley": "Pink"}) == "Pink"

def test_two_favorite_colors() -> None:
    """A test to see if when two diffreent colors are in the argument, it returns the color mentioned first as the favorite."""
    assert favorite_color({"Sally": "Blue", "Harry": "Green"}) == "Blue"

def test_three_favorite_colors() -> None:
    """A test to see if when three colors, one of which is mentioned twice, are in the argument, it returns the color mentioned twice as the favorite."""
    assert favorite_color({"Sally": "Blue", "Harry": "Green", "Arthur": "Green"}) == "Green"


def test_count_three_elements() -> None:
    """A test to see if when three str,one of which is mentioned twice, are in the argument, both are correctly counted for instances they are mentioned and returned as a dictionary."""
    assert count(list("a", "b", "a")) == {"a": 2, "b": 1}
    
def test_count_empty_list() -> None:
    """A test to see if when an empty list is the argument, an empty dictionary is returned."""
    assert count(list()) == {}
    
def test_count_three_same() -> None:
    """A test to see if when three of the same str are given as the argument, a dictionary counting the str designates the value as 3 to signify that is was mentioned three times."""
    assert count(list("b", "b", "b")) == {"b": 3}