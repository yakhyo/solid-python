## The Single Responsibility Principle (SRP)

**The Single Responsibility Principle (SRP)** is a design principle that is part of the SOLID acronym for
object-oriented
programming. It states that a class or module should have only one reason to change. In other words, a class should have
only one responsibility, and that responsibility should be encapsulated within that class.

The SRP aims to make code more modular, reusable, and maintainable. By separating responsibilities into separate classes
or modules, we can isolate changes to a particular functionality without affecting other parts of the codebase. This
makes it easier to test and refactor code.

Let's take an example to understand this principle better. Suppose we have a class Order that represents an order in an
e-commerce application. The Order class has several responsibilities, such as calculating the total price of the order,
applying discounts, and saving the order to the database. Here's an example code:

```python
class Order:
    def __init__(self, order_items):
        self.order_items = order_items
        self.total_price = self.calculate_total_price()
        self.apply_discount()
        self.save_order()

    def calculate_total_price(self):
        pass
        # code to calculate the total price of the order

    def apply_discount(self):
        pass
        # code to apply discounts to the order

    def save_order(self):
        pass
        # code to save the order to the database
```

In this example, the `Order` class has multiple responsibilities, including calculating the total price of the order,
applying discounts, and saving the order to the database. This violates the SRP because the `Order` class has more than
one reason to change. If we need to make changes to any of these responsibilities, we'll have to modify the `Order`
class,which can lead to code that is difficult to maintain and test.

To apply the SRP, we should separate these responsibilities into separate classes or modules. For example, we can create
a `OrderCalculator` class that is responsible for calculating the total price of an order, a `DiscountApplier` class
that applies discounts to an order, and a `OrderPersistence` class that saves orders to the database. Here's an updated
code:

```python
class Order:
    def __init__(self, order_items):
        self.order_items = order_items
        self.total_price = OrderCalculator.calculate_total_price(order_items)
        self.apply_discount()
        OrderPersistence.save_order(self)

    def apply_discount(self):
        pass
        # code to apply discounts to the order


class OrderCalculator:
    @staticmethod
    def calculate_total_price(order_items):
        pass
        # code to calculate the total price of the order


class DiscountApplier:
    @staticmethod
    def apply_discount(order):
        pass
        # code to apply discounts to the order


class OrderPersistence:
    @staticmethod
    def save_order(order):
        pass
        # code to save the order to the database

```

In this updated code, each class has a single responsibility. The `OrderCalculator` class is responsible for calculating
the total price of an order, the `DiscountApplier` class is responsible for applying discounts to an order, and the
`OrderPersistence` class is responsible for saving orders to the database. The `Order` class now delegates these
responsibilities to the appropriate classes, which makes the code easier to maintain, test, and extend.

In conclusion, the SRP is an important design principle that encourages us to write code that is modular, maintainable,
and extensible. By separating responsibilities into separate classes or modules, we can isolate changes to a particular
functionality without affecting other parts of the codebase.