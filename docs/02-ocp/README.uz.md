---
layout: default
title: "Open/Closed (UZ)"
nav_exclude: true
permalink: /uz/02-ocp/
---

{: .note }
> **Til:** [English]({{ site.baseurl }}/02-ocp/) | **O'zbek**

# Open/Closed Principle (OCP)

> Dasturiy tizimlar **kengaytirish uchun ochiq**, lekin **o'zgartirish uchun yopiq** bo'lishi kerak.

Yangi funksionallikni mavjud kodni o'zgartirmasdan qo'shish imkoni bo'lishi kerak.
Bunga odatda **inheritance** (meros olish) va **polymorphism** (polimorfizm) orqali erishiladi.

## Diagramma

<p align="center">
  <img src="{{ site.baseurl }}/assets/02-ocp.png" width="700" alt="OCP klass diagrammasi" style="border-radius: 12px;" />
</p>

## Noto'g'ri yondashuv

[`violation.py`](violation.py) dagi `AreaCalculator` har bir shakl turini `isinstance` tekshiruvi orqali aniqlaydi:

```python
class AreaCalculator:
    @staticmethod
    def calculate(shape: object) -> float:
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        if isinstance(shape, Circle):
            return math.pi * shape.radius ** 2
        raise TypeError(f"Unknown shape: {type(shape).__name__}")
```

`Triangle` qo'shish uchun mavjud `AreaCalculator` klassini o'zgartirish kerak — bu **o'zgartirish uchun yopiq emas**.

## To'g'ri yondashuv

[`correct.py`](correct.py) dagi `Shape` abstrakt klassi `area()` metodini belgilaydi.
Har bir shakl o'z hisob-kitobini mustaqil bajaradi:

```python
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height
```

Yangi shakl qo'shish — faqat yangi subklass yaratish. **Mavjud kodga hech qanday o'zgartirish kiritilmaydi.**
