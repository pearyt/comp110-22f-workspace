"""This is the utils part."""
__author__ = "730613916"


def only_evens(input_list: list[int]) -> list[int]:
    """Return a list of only even numbers."""
    why: list[int] = list()
    i: int = 0
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            why.append(input_list[i])
            i += 1
        else:  
            i += 1
    return why


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Add up two lists together into a combined list."""
    return_list: list[int] = list()
    i: int = 0
    w: int = 0
    while i < len(list_1):
        return_list.append(list_1[i])
        i += 1
    while w < len(list_2):
        return_list.append(list_2[w])
        w += 1
    return return_list


def sub(a_list: list[int], start_index: int, last_index: int) -> list[int]:
    """Using a list, return a subset list between start and end index."""
    if start_index < 0:
        start_index = 0
    if last_index > len(a_list):
        last_index = len(a_list)
    i = last_index - start_index
    new_list: list[int] = list()
    if len(a_list) == 0:
        return new_list
    elif start_index > len(a_list):
        return new_list
    elif last_index == 0:
        return new_list
    else:
        w: int = 0
        while w < i:
            new_list.append(a_list[start_index])
            start_index += 1
            w += 1
        return new_list