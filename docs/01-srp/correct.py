"""Single Responsibility Principle -- Correct.

Each class has exactly one reason to change:
  - Order:            holds order data
  - PriceCalculator:  pricing logic
  - DiscountApplier:  discount rules
  - OrderRepository:  persistence
"""

from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: float
    quantity: int


class PriceCalculator:
    @staticmethod
    def total(items: list[Item]) -> float:
        return sum(item.price * item.quantity for item in items)


class DiscountApplier:
    @staticmethod
    def apply(total: float) -> float:
        if total > 200:
            return total * 0.9
        return total


class OrderRepository:
    @staticmethod
    def save(order: "Order") -> None:
        print(f"[DB] Saving order — total: ${order.total_price:.2f}")


@dataclass
class Order:
    items: list[Item] = field(default_factory=list)
    total_price: float = 0.0

    def finalize(self) -> None:
        self.total_price = PriceCalculator.total(self.items)
        self.total_price = DiscountApplier.apply(self.total_price)
        OrderRepository.save(self)


if __name__ == "__main__":
    items = [Item("Keyboard", 75.00, 1), Item("Mouse", 50.00, 3)]
    order = Order(items=items)
    order.finalize()
    print(f"Order total: ${order.total_price:.2f}")
