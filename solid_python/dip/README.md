## Dependency Inversion Principle (DIP)

The **Dependency Inversion Principle (DIP)** is a principle in object-oriented programming that states that high-level
modules should not depend on low-level modules, but both should depend on abstractions. The principle also states that
abstractions should not depend on details, but details should depend on abstractions.

In other words, instead of depending on concrete implementations of classes and modules, we should depend on abstract
interfaces or classes that define the behavior of these modules. This allows us to decouple modules and create more
flexible and maintainable software systems.

The DIP is one of the five SOLID principles of object-oriented design, which aim to create more maintainable and
flexible software systems. The DIP is important because it promotes code that is more modular, flexible, and extensible,
which makes it easier to understand, test, and modify.

To apply the DIP, we should follow these guidelines:

High-level modules should not depend on low-level modules, but both should depend on abstractions. This means that we
should define abstract interfaces or classes that define the behavior of our modules, and have our high-level modules
depend on these abstractions rather than on the concrete implementations of the low-level modules.

Abstractions should not depend on details, but details should depend on abstractions. This means that our abstract
interfaces or classes should not depend on concrete implementation details, but rather on more general abstractions that
can be implemented in many different ways.

By following these guidelines, we can create code that is more modular, flexible, and extensible. We can also more
easily swap out different implementations of our modules without having to change our high-level modules, which makes
our code more maintainable and scalable. Additionally, we can more easily test our code by creating mock objects that
implement the same abstractions as our real modules, but with simpler and more predictable behavior.

```python
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} with cash")


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paying {amount} with credit card")


class PaymentProcessor:
    def __init__(self, payment):
        self.payment = payment

    def process_payment(self, amount):
        self.payment.pay(amount)


cash_payment = CashPayment()
credit_card_payment = CreditCardPayment()

processor1 = PaymentProcessor(cash_payment)
processor1.process_payment(100)

processor2 = PaymentProcessor(credit_card_payment)
processor2.process_payment(200)

```

In this example, we have defined an abstract Payment class that defines a pay method. This is our abstraction that
high-level modules can depend on. We then define two concrete implementations of this Payment class - CashPayment and
CreditCardPayment.

We then define a PaymentProcessor class that takes a Payment object in its constructor. This is our high-level module
that depends on our abstraction rather than on the concrete implementations.

Finally, we create two instances of PaymentProcessor, one with a CashPayment object and one with a CreditCardPayment
object, and call the process_payment method on each one with a different amount.

This implementation allows us to swap out different implementations of the Payment class without having to change our
PaymentProcessor class. It also allows us to easily test our code by creating mock Payment objects that implement the
same interface as our real Payment objects.
