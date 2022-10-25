"""This is the dictionary exercises for ex07."""
__author__: str = "730613916"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert function will reverse the positions of the key and value in the list."""
    new_dict: dict[str, str] = dict()
    for key in input:
        new_dict[input[key]] = key
    if len(input) != len(new_dict):
        raise KeyError("KeyError")
    return new_dict


def favorite_color(color_dict: dict[str, str]) -> str: 
    """Take an input dictionary and return most used color."""
    i: int = 0
    new_dict: dict[str, int] = {}
    number_count: int = 0
    most_color: str = ""
    for key in color_dict:
        if color_dict[key] in new_dict:
            number_count += 1
            new_dict[color_dict[key]] += 1
        else:
            new_dict[color_dict[key]] = 1 
    for index in new_dict:
        if new_dict[index] > i:
            i = new_dict[index]
            most_color = index
    return most_color


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