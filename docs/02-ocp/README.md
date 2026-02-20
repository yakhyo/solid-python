---
layout: default
title: "Open/Closed"
nav_order: 3
permalink: /02-ocp/
---

{: .note }
> **Language:** **English** | [O'zbek]({{ site.baseurl }}/uz/02-ocp/)

# Open/Closed Principle (OCP)

> Software entities should be **open for extension** but **closed for modification**.

You should be able to add new behavior without editing existing, tested code.
This is typically achieved through **inheritance** and **polymorphism**.

## Diagram

<p align="center">
  <img src="{{ site.baseurl }}/assets/02-ocp.png" width="700" alt="OCP class diagram" style="border-radius: 12px;" />
</p>

## Violation

In [`violation.py`](violation.py) an `AreaCalculator` uses `isinstance` checks to handle each shape type:

```python
class AreaCalculator:
    @staticmethod
    def calculate(shape: object) -> float:
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        if isinstance(shape, Circle):
            return math.pi * shape.radius ** 2
        raise TypeError(f"Unknown shape: {type(shape).__name__}")
```

Adding a `Triangle` requires modifying the existing `AreaCalculator` — it is **not closed for modification**.

## Correct

In [`correct.py`](correct.py) a `Shape` abstract base class defines the `area()` contract.
Each shape implements its own calculation:

```python
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height
```

Adding a new shape is just a new subclass — **zero changes to existing code**.
