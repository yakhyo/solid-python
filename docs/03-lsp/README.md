---
layout: default
title: "Liskov Substitution"
nav_order: 4
permalink: /03-lsp/
---

{: .note }
> **Language:** **English** | [O'zbek]({{ site.baseurl }}/uz/03-lsp/)

# Liskov Substitution Principle (LSP)

> Subtypes must be **substitutable** for their base types without altering program correctness.

If code works with a base class, it must continue to work correctly with any subclass — no surprises, no broken contracts.

## Diagram

<p align="center">
  <img src="{{ site.baseurl }}/assets/03-lsp.png" width="700" alt="LSP class diagram" style="border-radius: 12px;" />
</p>

## Violation

In [`violation.py`](violation.py) `Square` inherits from `Rectangle` and overrides the setters to keep width and height equal.
This introduces a **side-effect** that violates the behavioral contract of `Rectangle`:

```python
class Square(Rectangle):
    def set_width(self, width: float) -> None:
        self._width = width
        self._height = width   # side-effect!

    def set_height(self, height: float) -> None:
        self._width = height   # side-effect!
        self._height = height
```

Any code that independently sets width and height on a `Rectangle` will get wrong results when handed a `Square`:

```python
def resize_rectangle(rect: Rectangle, width: float, height: float) -> float:
    rect.set_width(width)
    rect.set_height(height)
    expected = width * height
    actual = rect.area()
    assert actual == expected  # fails for Square!
```

## Correct

In [`correct.py`](correct.py) both `Rectangle` and `Square` inherit from a common `Shape` abstraction.
Each shape owns its geometry without pretending to be something it is not:

```python
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
        return self.side ** 2
```

Both can be passed anywhere a `Shape` is expected — **no behavioral surprises**.
