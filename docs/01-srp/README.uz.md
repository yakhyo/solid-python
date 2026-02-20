---
layout: default
title: "Single Responsibility (UZ)"
nav_exclude: true
permalink: /uz/01-srp/
---

{: .note }
> **Til:** [English]({{ site.baseurl }}/01-srp/) | **O'zbek**

# Single Responsibility Principle (SRP)

> Har bir klass faqat **bitta o'zgarish sababiga** ega bo'lishi kerak.

Har bir klass yoki modul **bitta vazifani** bajarishi lozim.
Agar bitta klass bir nechta vazifani bajara boshlasa (masalan, biznes-logika, ma'lumotlarni saqlash, formatlash), ulardan birortasi o'zgarganda butun klassni qayta yozish va test qilish kerak bo'ladi.

## Diagramma

<p align="center">
  <img src="{{ site.baseurl }}/assets/01-srp.png" width="700" alt="SRP klass diagrammasi" style="border-radius: 12px;" />
</p>

## Noto'g'ri yondashuv

[`violation.py`](violation.py) dagi `Order` klassi uchta turli vazifani bajaradi:

- **Narxni hisoblash** — buyurtma summasini hisoblash
- **Chegirma** — biznes-qoidalari bo'yicha chegirma qo'llash
- **Saqlash** — buyurtmani bazaga saqlash

```python
class Order:
    def __init__(self, items: list[Item]) -> None:
        self.items = items
        self.total_price = self.calculate_total()
        self.total_price = self.apply_discount(self.total_price)
        self.save()
```

Chegirma qoidalari, narx formulasi yoki saqlash tizimi o'zgarganda — aynan shu bitta klassni o'zgartirish kerak bo'ladi.

## To'g'ri yondashuv

[`correct.py`](correct.py) dagi har bir vazifa alohida klassga ajratilgan:

| Klass | Vazifasi |
|-------|----------|
| `Order` | Buyurtma ma'lumotlarini saqlaydi |
| `PriceCalculator` | Umumiy narxni hisoblaydi |
| `DiscountApplier` | Chegirma qoidalarini qo'llaydi |
| `OrderRepository` | Bazaga saqlash bilan shug'ullanadi |

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

Endi har bir klassning **faqat bitta o'zgarish sababi** bor va ularni mustaqil ravishda test qilish, kengaytirish yoki almashtirish mumkin.
