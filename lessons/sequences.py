"""Notes and examples of tuple and range sequence types."""

# Declaring a type alias that "invents" the Point2D type
"""We use camel casing - where we use a capital letter to signify new words - for tuple."""
Point2D = tuple[float, float]


start_position: Point2D = (5.0, 10.0)

"""Below makes a NEW tuple --> we can't actually modify the original tuple."""
start_position = (start_position[0] + 5.0, start_position[1] + 10.0)

end_position: Point2D = (99.0, 99.0)


# because tuples are a sequence, they are 0-indexed
print(start_position[0])

for item in end_position:
    print(item)

print(len(end_position))



# Examples of ranges
"""Never call a variable name range!"""
a_range: range = range(0, 10, 3)
"""start is 0, stop is 10, increment is 3; produces range of object"""
# Below we are accessing the items of a range:
print(a_range[0])
print(a_range[1])
print(len(a_range))
for i in a_range:
    print(i)
    """We commonly use i instead of item in this!"""

# An example of using the default parameter step where the default step is 1
another_range: range = range(0, 10)

# If you only pass one argument to the range, it specifies the stop marker with such value (and start value is 0 by default!)
zero_start: range = range(10)
for x in zero_start:
    print(x)


names: list[str] = ["Kris", "Alyssa", "Ben", "Arnold"]

for name in names:
    print(name)

"""To print only certain names (w an increment of 2 instead"""
# Range is often used to write for loops where your iteration pattern is NOT consecutive!
print("Every other")
for i in range(0, len(names), 2):
    print(names[i])