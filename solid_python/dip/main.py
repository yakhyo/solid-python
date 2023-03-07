"""
The **Dependency Inversion Principle (DIP)** is a principle in
object-oriented programming that states that high-level modules
should not depend on low-level modules, but both should depend
on abstractions. The principle also states that abstractions should
not depend on details, but details should depend on abstractions.
"""

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

"""

In this example, we have defined an abstract Payment class that 
defines a pay method. This is our abstraction that high-level modules
can depend on. We then define two concrete implementations of this 
Payment class - CashPayment and CreditCardPayment.

We then define a PaymentProcessor class that takes a Payment object in
its constructor. This is our high-level module that depends on our 
abstraction rather than on the concrete implementations.

Finally, we create two instances of PaymentProcessor, one with a 
CashPayment object and one with a CreditCardPayment object, and call 
the process_payment method on each one with a different amount.

This implementation allows us to swap out different implementations of 
the Payment class without having to change our PaymentProcessor class. 
It also allows us to easily test our code by creating mock Payment objects 
that implement the same interface as our real Payment objects.
"""
