"""Open/Closed Principle -- Violation.

AreaCalculator uses if/elif to handle each shape type.  Adding a new
shape (e.g. Triangle) forces us to modify the existing calculator — the
class is NOT closed for modification.
"""

import math


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius


class AreaCalculator:
    """Must be edited every time a new shape is introduced."""

    @staticmethod
    def calculate(shape: object) -> float:
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        if isinstance(shape, Circle):
            return math.pi * shape.radius**2
        raise TypeError(f"Unknown shape: {type(shape).__name__}")


if __name__ == "__main__":
    shapes: list[object] = [Rectangle(5, 10), Circle(7)]
    for s in shapes:
        print(f"{type(s).__name__}: {AreaCalculator.calculate(s):.2f}")
