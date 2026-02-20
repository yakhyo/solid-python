"""Dependency Inversion Principle -- Violation.

PaymentProcessor directly instantiates and depends on the concrete
CreditCardPayment class.  Switching to cash or adding a new payment
method requires modifying PaymentProcessor itself.
"""


class CreditCardPayment:
    def pay(self, amount: float) -> None:
        print(f"Paying ${amount:.2f} with credit card")


class PaymentProcessor:
    """High-level module tightly coupled to a low-level concrete class."""

    def __init__(self) -> None:
        self.payment = CreditCardPayment()  # hard-wired dependency

    def process(self, amount: float) -> None:
        self.payment.pay(amount)


if __name__ == "__main__":
    processor = PaymentProcessor()
    processor.process(150.00)
