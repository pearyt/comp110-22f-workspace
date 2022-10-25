"""This is the dictionary function tests for ex07."""
__author__: str = "730613916"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_dict() -> None: 
    """Test the invert function if it works with a short dictionary."""
    input: dict[str, str] = {"bob": "tom"}
    assert invert(input) == {"tom": "bob"}
    

def test_longer_list_dict() -> None: 
    """Testing a dictionary with more than 2 terms."""
    input: dict[str, str] = {"actor": "Kim", "President": "Bob", "teacher": "Mr. G", "kid": "brother"}
    assert invert(input) == {"Kim": "actor", "Bob": "President", "Mr. G": "teacher", "brother": "kid"}


def test_key_error() -> None:
    """Testing if the function raises key error."""
    with pytest.raises(KeyError):
        input = {'kris': 'jordan', 'michael': 'jordan'}
        invert(input)


def test_favorite_color_into_list() -> None: 
    """Testing to split dictionary into list."""
    color_dict: dict[str, str] = {"bob": "blue", "tim": "orange", "gary": "blue"}
    assert favorite_color(color_dict) == "blue"


def test_favorite_color_into_list_2() -> None: 
    """Counting the colors."""
    color_dict: dict[str, str] = {"bob": "blue", "tim": "orange", "tom": "blue", "gary": "orange"}
    assert favorite_color(color_dict) == "blue"


def test_favorite_color_into_list_3() -> None: 
    """Testing same number of colors."""
    color_dict: dict[str, str] = {"bob": "purple", "tim": "orange", "gary": "pink", "bib": "white"}
    assert favorite_color(color_dict) == "purple"


def test_function_3_count() -> None: 
    """Test if the function returns dictionary with count."""
    input: list[str] = ["bob", "bob", "tom", "kim"]
    assert count(input) == {"bob": 2, "tom": 1, "kim": 1}


def test_function_4_count() -> None: 
    """Test if the function returns dictionary with count."""
    input: list[str] = ["bob", "bob", "bob", "kim", "tim", "larry", "sponge"]
    assert count(input) == {"bob": 3, "tim": 1, "kim": 1, "tim": 1, "larry": 1, "sponge": 1}


def test_function_5_count() -> None: 
    """Test if the function returns dictionary with count."""
    input: list[str] = ["bob", "bob", "asd"]
    assert count(input) == {"bob": 2, "asd": 1}