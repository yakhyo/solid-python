---
layout: default
title: "Dependency Inversion"
nav_order: 6
permalink: /05-dip/
---

{: .note }
> **Language:** **English** | [O'zbek]({{ site.baseurl }}/uz/05-dip/)

# Dependency Inversion Principle (DIP)

> High-level modules should not depend on low-level modules. Both should depend on **abstractions**.

Instead of hard-wiring concrete classes, use **dependency injection** to pass abstractions.
This decouples components and makes the system easier to test and extend.

## Diagram

<p align="center">
  <img src="{{ site.baseurl }}/assets/05-dip.png" width="700" alt="DIP class diagram" style="border-radius: 12px;" />
</p>

## Violation

In [`violation.py`](violation.py) `PaymentProcessor` directly creates a `CreditCardPayment` inside its constructor:

```python
class PaymentProcessor:
    def __init__(self) -> None:
        self.payment = CreditCardPayment()  # hard-wired dependency

    def process(self, amount: float) -> None:
        self.payment.pay(amount)
```

Switching to cash or cryptocurrency requires modifying the processor itself.

## Correct

In [`correct.py`](correct.py) both the processor and payment methods depend on a `Payment` abstraction:

```python
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None: ...

class PaymentProcessor:
    def __init__(self, payment: Payment) -> None:
        self.payment = payment

    def process(self, amount: float) -> None:
        self.payment.pay(amount)
```

New payment methods are added by implementing `Payment` — **the processor never changes**:

```python
for method in (CashPayment(), CreditCardPayment(), CryptoPayment()):
    processor = PaymentProcessor(method)
    processor.process(150.00)
```
