"""An exercise for dictionaries where I implement function skeletons."""
__author__ = "730604478"

def invert(a: dict[str, str]) -> dict[str, str]:
    """A function to invert the keys and values of a given dictionary."""
    inverted: dict[str, str] = {}
    existing_values: list[str] = []
    for key in a:
        value = a[key]
        inverted[value] = key
        for x in existing_values:
            if x == value:
                raise KeyError("Sorry, there was more than one key detected!")
        existing_values.append(value)
    return inverted


def favorite_color(a: dict[str, str]) -> str:
    """A function to designate the color mentioned most frequently in a given dictionary of strings, to return that color's name as a str."""
    existing_colors: dict[str, int] = {}
    for name in a:
        color = a[name]
        if color in existing_colors.keys():
            existing_colors[color] += 1
        else:
            existing_colors[color] = 1
    max_nbr: int = 0
    max_key: str = ""
    for color1 in existing_colors:
        if max_nbr < existing_colors[color1]:
            max_nbr = existing_colors[color1]
            max_key = color1
    return max_key


def count(a: list[str]) -> dict[str, int]:
    """A function to count the number of instances a certain str is given in a list, and return the matching pairs of str (key) and instances (value) as a dictionary."""
    result: dict[str, int] = {}
    for item in a:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
        return result 