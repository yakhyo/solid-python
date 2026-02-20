"""Open/Closed Principle -- Correct.

Shape defines an abstract `area()` method.  New shapes are added by
creating a subclass — no existing code needs to change.
"""

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


def total_area(shapes: list[Shape]) -> float:
    return sum(s.area() for s in shapes)


if __name__ == "__main__":
    shapes: list[Shape] = [Rectangle(5, 10), Circle(7), Triangle(6, 8)]
    for s in shapes:
        print(f"{type(s).__name__}: {s.area():.2f}")
    print(f"Total area: {total_area(shapes):.2f}")
