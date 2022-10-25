"""This is using lists to create functions."""
__author__ = "730613916"


def all(input_list: list[int], match: int) -> bool:
    """All function: returns a bool true or false whether all the numbers in a list are matching."""
    list_index: int = 0
    all_bool: bool = False
    while list_index < len(input_list):
        if input_list[list_index] == match:
            all_bool = True
            list_index += 1          
        else:
            all_bool = False
            list_index += len(input_list)
            return all_bool
    return all_bool


def max(input_int_list: list[int]) -> int:
    """Max function: given a list of integers, return the maximum."""
    if len(input_int_list) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        index_list = 0
        b = index_list + 1 
        max_index: int = 0
        while b < len(input_int_list):
            if input_int_list[index_list] >= input_int_list[b]:
                max_index = input_int_list[index_list]
                b += 1   
            else:
                max_index = input_int_list[b]
                index_list += 1              
    return max_index


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Is_equal function: if every index in two lists are the exact same, print true.""" 
    is_equal_bool: bool = True
    if len(list_1) != len(list_2):
        is_equal_bool = False
        return is_equal_bool
    else: 
        i = 0 
        while i < len(list_1):
            if list_1[i] == list_2[i]:
                i += 1
            else: 
                is_equal_bool = False
                i += len(list_1)
    return is_equal_bool