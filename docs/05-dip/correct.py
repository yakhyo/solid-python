"""Dependency Inversion Principle -- Correct.

Both the high-level PaymentProcessor and the low-level payment classes
depend on the Payment abstraction.  New payment methods are added
without touching the processor.
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None: ...


class CashPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Paying ${amount:.2f} with cash")


class CreditCardPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Paying ${amount:.2f} with credit card")


class CryptoPayment(Payment):
    def pay(self, amount: float) -> None:
        print(f"Paying ${amount:.2f} with cryptocurrency")


class PaymentProcessor:
    """High-level module depends on the Payment abstraction, not concrete classes."""

    def __init__(self, payment: Payment) -> None:
        self.payment = payment

    def process(self, amount: float) -> None:
        self.payment.pay(amount)


if __name__ == "__main__":
    for method in (CashPayment(), CreditCardPayment(), CryptoPayment()):
        processor = PaymentProcessor(method)
        processor.process(150.00)
