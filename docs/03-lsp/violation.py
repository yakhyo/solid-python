"""Liskov Substitution Principle -- Violation.

Rectangle has `set_width` / `set_height` that can be called independently.
Square overrides both so that width and height always stay equal.

This breaks the behavioral contract: code that sets width and height
separately on a "Rectangle" will get wrong results when handed a Square.
"""


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    def set_width(self, width: float) -> None:
        self._width = width

    def set_height(self, height: float) -> None:
        self._height = height

    def area(self) -> float:
        return self._width * self._height


class Square(Rectangle):
    """Violates LSP: overrides setters to enforce equal sides."""

    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    def set_width(self, width: float) -> None:
        self._width = width
        self._height = width  # side-effect — breaks Rectangle's contract

    def set_height(self, height: float) -> None:
        self._width = height  # side-effect — breaks Rectangle's contract
        self._height = height


def resize_rectangle(rect: Rectangle, width: float, height: float) -> float:
    """Expects Rectangle's independent width/height contract."""
    rect.set_width(width)
    rect.set_height(height)
    expected = width * height
    actual = rect.area()
    assert actual == expected, f"LSP violation! Expected {expected}, got {actual}"
    return actual


if __name__ == "__main__":
    rect = Rectangle(2, 3)
    print(f"Rectangle: {resize_rectangle(rect, 5, 10)}")  # 50 ✓

    sq = Square(5)
    print(f"Square:    {resize_rectangle(sq, 5, 10)}")  # AssertionError!
