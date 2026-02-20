"""Liskov Substitution Principle -- Correct.

Instead of making Square a subtype of Rectangle (and breaking the
setter contract), both inherit from a common Shape abstraction.
Each shape computes its own area without pretending to be another shape.
"""

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


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2


def print_area(shape: Shape) -> None:
    print(f"{type(shape).__name__}: area = {shape.area():.2f}")


if __name__ == "__main__":
    shapes: list[Shape] = [Rectangle(5, 10), Square(7)]
    for s in shapes:
        print_area(s)
