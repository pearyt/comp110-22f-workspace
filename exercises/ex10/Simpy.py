"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730613916"


class Simpy:
    """Simpy class."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, items: list[float]):
        """Initialize the object."""
        self.values = items
    
    def __repr__(self) -> str:
        """Print as a str magic method."""
        return f"Simpy({self.values})"
    
    def fill(self, item: float, int: int) -> None:
        """Method to fill sympy object with certain number of floats."""
        self.values = []
        for _ in range(0, int):
            self.values.append(item)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Order the simpy list by certian intervals."""
        assert step != 0.0
        i: int = 0
        while i < (stop / step):
            self.values.append(start)
            start += step
            if abs(start) >= abs(stop):
                i += (stop / step)
            i += 1
    
    def sum(self) -> float:
        """Sum up all of the items in the list."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Addition magic method for Simpy objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                bob = self.values[i] + rhs
                result.values.append(bob)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                mol = self.values[i] + rhs.values[i]
                result.values.append(mol)
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Multiplication magic method for Simpy objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                bob = self.values[i] ** rhs
                result.values.append(bob)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                mol = self.values[i] ** rhs.values[i]
                result.values.append(mol)
        return result
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Equal to or not magic method for Simpy objects."""
        result: list = []
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                if self.values[i] == rhs:
                    result.append(True)
                else: 
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Greater than magic method."""
        result: list = []
        if isinstance(rhs, float):
            for i in range(len(self.values)):
                if self.values[i] > rhs:
                    result.append(True)
                else: 
                    result.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]: 
        """Get item magic method for indexing Simpy object's list."""
        if isinstance(rhs, int):
            return self.values[rhs]       
        else:
            result: Simpy = Simpy([])
            for i in range(len(self.values)):
                if rhs[i] is True:
                    result.values.append(self.values[i])
            return result