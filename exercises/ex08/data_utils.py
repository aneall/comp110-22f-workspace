"""Dictionary related utility functions."""

__author__ = "730604478"


from ast import Dict
from csv import DictReader

# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a table (which is a list of dictionaries)."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8") # inferring type of variable; "r" stands for read

    # Prepare to read the data file as a CSV rather than just strings^^
    csv_reader = DictReader(file_handle)

    # looping through each of the row; this reads through each row of the CSV file line-by-line
    for row in csv_reader:
        result.append(row)

    # Then close the file when done to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """To produce a list[str] of all values in a single column."""
    column_list: list[str] = []
    for row in table:
        item: str = row[column]
        column_list.append(item)
    return column_list


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """This function transforms a row-oriented table representation --> to a column-oriented table representation."""
    # loop over all of the columns and call the function to get back all the values for a specific function:
    column_table: dict[str, list[str]] = {} # {} is a dictionary literal

    # we can find column names by looping over 1st row
    column_name_row: dict[str, str] = row_table[0] # the first row is the name of the columns (the 1st dictionary)
    for column in column_name_row:
        column_table[column] = column_values(row_table, column)

    return column_table


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    new_table: dict[str, list[str]] = {}

    for column in column_table:
        first_n: list[str] = []
        for index in range(N):
            first_n.append(column_table[column][index])
        new_table[column] = first_n
    return new_table


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = column_table[column]
    return result


def concat(column_table1: dict[str, list[str]], column_table2: dict[str, list[str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}

    for column in column_table1:
        result[column] = column_table1[column]

    for column in column_table2:
        if column in result:
            result[column] += column_table2[column]
        else:
            result[column] = column_table2[column]
    return result

# GO BACK TO FINISH THIS ^^^^^

def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

        

