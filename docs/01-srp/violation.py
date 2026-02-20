"""Single Responsibility Principle -- Violation.

The Order class below handles three unrelated concerns:
  1. Price calculation
  2. Discount logic
  3. Database persistence

Any change to the discount rules, the pricing formula, or the storage
backend forces a modification to this single class.
"""

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    quantity: int


class Order:
    """Violates SRP: one class, three reasons to change."""

    def __init__(self, items: list[Item]) -> None:
        self.items = items
        self.total_price = self.calculate_total()
        self.total_price = self.apply_discount(self.total_price)
        self.save()

    def calculate_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)

    def apply_discount(self, total: float) -> float:
        if total > 200:
            return total * 0.9
        return total

    def save(self) -> None:
        print(f"[DB] Saving order — total: ${self.total_price:.2f}")


if __name__ == "__main__":
    items = [Item("Keyboard", 75.00, 1), Item("Mouse", 50.00, 3)]
    order = Order(items)
    print(f"Order total: ${order.total_price:.2f}")
