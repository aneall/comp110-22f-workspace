"""Some helpful utility functions for working with CSV files."""

from ast import Dict
from csv import DictReader

# setting up a utilities file to use in this function and in a later exercise!
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
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """This function transforms a row-oriented table representation --> to a column-oriented table representation."""
    # loop over all of the columns and call the function to get back all the values for a specific function:
    result: dict[str, list[str]] = {} # {} is a dictionary literal

    # we can find column names by looping over 1st row
    first_row: dict[str, str] = row_table[0] # the first row is the name of the columns (the 1st dictionary)
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result