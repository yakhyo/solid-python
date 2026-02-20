---
layout: default
title: "Dependency Inversion (UZ)"
nav_exclude: true
permalink: /uz/05-dip/
---

{: .note }
> **Til:** [English]({{ site.baseurl }}/05-dip/) | **O'zbek**

# Dependency Inversion Principle (DIP)

> Yuqori darajadagi modullar quyi darajadagi modullarga bog'liq bo'lmasligi kerak. Ikkalasi ham **abstraktsiyalarga** bog'liq bo'lishi kerak.

Konkret klasslarni to'g'ridan-to'g'ri ishlatish o'rniga, **dependency injection** orqali abstraktsiyalarni bering.
Bu komponentlar orasidagi bog'liqlikni kamaytiradi va tizimni test qilish hamda kengaytirishni osonlashtiradi.

## Diagramma

<p align="center">
  <img src="{{ site.baseurl }}/assets/05-dip.png" width="700" alt="DIP klass diagrammasi" style="border-radius: 12px;" />
</p>

## Noto'g'ri yondashuv

[`violation.py`](violation.py) dagi `PaymentProcessor` konstruktorida `CreditCardPayment`'ni to'g'ridan-to'g'ri yaratadi:

```python
class PaymentProcessor:
    def __init__(self) -> None:
        self.payment = CreditCardPayment()  # qattiq bog'liqlik

    def process(self, amount: float) -> None:
        self.payment.pay(amount)
```

Naqd pul yoki kriptovalyutaga o'tish uchun `PaymentProcessor`'ning o'zini o'zgartirish kerak bo'ladi.

## To'g'ri yondashuv

[`correct.py`](correct.py) da esa `PaymentProcessor` ham, to'lov usullari ham `Payment` abstraktsiyasiga bog'liq:

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

Yangi to'lov usulini qo'shish uchun faqat `Payment`'ni implement qilish kifoya — **`PaymentProcessor` hech qachon o'zgarmaydi**:

```python
for method in (CashPayment(), CreditCardPayment(), CryptoPayment()):
    processor = PaymentProcessor(method)
    processor.process(150.00)
```
