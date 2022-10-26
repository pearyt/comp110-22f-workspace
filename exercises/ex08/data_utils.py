"""Dictionary related utility functions."""

__author__ = "730613916"

# Define your functions below
from csv import DictReader
from unittest import result

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding = "utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result 


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""   
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result 


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """List only a few rows."""
    result: dict[str, list[str]] = {}
    for row in table:
        N_list: list[str] = []
        for i in range(rows):
            item: str = table[row][i]
            N_list.append(item)
        result[row] = N_list

    return result


def select(row_table: dict[str, list[str]], choice: list[str]) -> dict[str, list[str]]:
    """Select only the wanted columns from the input."""
    result: dict[str, list[str]] = {}
    for choice in row_table:
        result[choice] = row_table[choice]
    return result


def concat(table_1: dict[str, list[str]] , table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Join together two separate tables of data."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column_1 in table_2:
        if column_1 in result:
            item: list[str] = table_2[column_1]
            result[column_1] = result[column] + item
        result[column_1] = table_2[column_1]
    return result


def count(input: list[str]) -> dict[str, int]:
    """Count the number of times a string occurs."""
    val_count: int = 0
    count_dict: dict[str, int] = {}
    for x in input:
        if x in count_dict:
            val_count += 1
            count_dict[x] += 1
        else: 
            count_dict[x] = 1
    return count_dict