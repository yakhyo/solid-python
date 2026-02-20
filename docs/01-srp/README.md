---
layout: default
title: "Single Responsibility"
nav_order: 2
permalink: /01-srp/
---

{: .note }
> **Language:** **English** | [O'zbek]({{ site.baseurl }}/uz/01-srp/)

# Single Responsibility Principle (SRP)

> A class should have only one reason to change.

Each class or module should encapsulate a **single responsibility**.
When a class handles multiple concerns (e.g. business logic, persistence, formatting), a change in any one area forces the entire class to be modified and re-tested.

## Diagram

<p align="center">
  <img src="{{ site.baseurl }}/assets/01-srp.png" width="700" alt="SRP class diagram" style="border-radius: 12px;" />
</p>

## Violation

In [`violation.py`](violation.py) the `Order` class handles three unrelated responsibilities:

- **Price calculation** — computing the order total
- **Discount logic** — applying business discount rules
- **Persistence** — saving the order to a database

```python
class Order:
    def __init__(self, items: list[Item]) -> None:
        self.items = items
        self.total_price = self.calculate_total()
        self.total_price = self.apply_discount(self.total_price)
        self.save()
```

Any change to discount rules, pricing formulas, or storage backends forces modification of this single class.

## Correct

In [`correct.py`](correct.py) each responsibility is extracted into its own class:

| Class | Responsibility |
|-------|---------------|
| `Order` | Holds order data |
| `PriceCalculator` | Computes the total price |
| `DiscountApplier` | Applies discount rules |
| `OrderRepository` | Handles persistence |

```python
@dataclass
class Order:
    items: list[Item] = field(default_factory=list)
    total_price: float = 0.0

    def finalize(self) -> None:
        self.total_price = PriceCalculator.total(self.items)
        self.total_price = DiscountApplier.apply(self.total_price)
        OrderRepository.save(self)
```

Now each class has exactly **one reason to change**, and they can be tested, extended, or replaced independently.
