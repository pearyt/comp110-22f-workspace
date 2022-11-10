"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730613916"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, point_2: Point) -> float:
        """Find the distance between two Points."""
        distance: float = sqrt((point_2.x - self.x) ** 2 + (point_2.y - self.y) ** 2)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def contract_disease(self) -> None:
        """Make a cell become sick."""
        self.sickness = constants.INFECTED

    def tick(self) -> None:
        """Update cell's location every second."""
        self.location = self.location.add(self.direction)
        if self.sickness >= constants.INFECTED:
            self.sickness += 1
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.immunize()

    def is_vulnerable(self) -> bool:
        """Check if a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Check if a cell is infected."""
        if self.sickness >= 1:
            return True
        else: 
            return False
    
    def contact_with(self, cell_2: Cell) -> None:
        """Infect cells if they make contact."""
        if self.is_infected() and cell_2.is_vulnerable():
            cell_2.contract_disease()
        elif self.is_vulnerable() and cell_2.is_infected():
            self.contract_disease()

    def immunize(self) -> None:
        """Change a cell's status to immune."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Check if a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
    
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected() is True:  
            return "pink"
        elif self.is_immune() is True:
            return "blue"
        elif self.is_vulnerable() is True:
            return "gray"
        else:
            return "black"


class Model:
    """The state of the simulation."""
    population: list[Cell]
    time: int = 0
    int: int 

    def __init__(self, cells: int, speed: float, int: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if int <= 0:
            raise ValueError("An integer number of cells must begin infected.")
        elif int >= cells:
            raise ValueError("An integer number of infected cells must be less than the total number of cells.")
        elif immune_cells < 0:
            raise ValueError("Enter a whole number integer of immune cells.")
        elif immune_cells >= cells:
            raise ValueError("Enter a number of immune cells less than total number of cells.")
        else:
            for _ in range(cells - (int + immune_cells)):
                start_location: Point = self.random_location()
                start_direction: Point = self.random_direction(speed)
                cell: Cell = Cell(start_location, start_direction)
                self.population.append(cell)
            for _ in range(int):
                start_location = self.random_location()
                start_direction = self.random_direction(speed)
                sick: Cell = Cell(start_location, start_direction)
                sick.contract_disease()
                self.population.append(sick)
            for _ in range(immune_cells):
                start_location = self.random_location()
                start_direction = self.random_direction(speed)
                immune: Cell = Cell(start_location, start_direction)
                immune.immunize()
                self.population.append(immune)
               
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()
            
    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = random() * 2.0 * pi
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)
    
    def check_contacts(self) -> None:
        """Check if two cells collide with each other."""
        for index in range(len(self.population)):
            for var in range(index + 1, len(self.population)):
                if self.population[index].location.distance(self.population[var].location) < constants.CELL_RADIUS:
                    self.population[index].contact_with(self.population[var])
                   
    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
        
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.sickness >= constants.INFECTED:
                return False
        return True