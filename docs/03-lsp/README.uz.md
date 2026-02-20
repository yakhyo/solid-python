---
layout: default
title: "Liskov Substitution (UZ)"
nav_exclude: true
permalink: /uz/03-lsp/
---

{: .note }
> **Til:** [English]({{ site.baseurl }}/03-lsp/) | **O'zbek**

# Liskov Substitution Principle (LSP)

> Quyi turlar (subtype'lar) asosiy turlar (base type'lar) **o'rnida ishlatilganda** dasturning to'g'ri ishlashiga ta'sir qilmasligi kerak.

Agar kod asosiy klass bilan ishlasa, uning istalgan subklassi bilan ham to'g'ri ishlashi shart — kutilmagan xatti-harakatlar bo'lmasligi kerak.

## Diagramma

<p align="center">
  <img src="{{ site.baseurl }}/assets/03-lsp.png" width="700" alt="LSP klass diagrammasi" style="border-radius: 12px;" />
</p>

## Noto'g'ri yondashuv

[`violation.py`](violation.py) dagi `Square` klassi `Rectangle`'dan meros oladi va setter'larni override qiladi — width va height doimo teng bo'lishi uchun. Bu `Rectangle`'ning xatti-harakat shartnomasini buzadi:

```python
class Square(Rectangle):
    def set_width(self, width: float) -> None:
        self._width = width
        self._height = width   # kutilmagan nojo'ya ta'sir!

    def set_height(self, height: float) -> None:
        self._width = height   # kutilmagan nojo'ya ta'sir!
        self._height = height
```

Width va height'ni mustaqil ravishda o'rnatadigan har qanday kod `Square` berilganda noto'g'ri natija beradi:

```python
def resize_rectangle(rect: Rectangle, width: float, height: float) -> float:
    rect.set_width(width)
    rect.set_height(height)
    expected = width * height
    actual = rect.area()
    assert actual == expected  # Square uchun xatolik!
```

## To'g'ri yondashuv

[`correct.py`](correct.py) dagi `Rectangle` va `Square` ikkisi ham umumiy `Shape` abstraktsiyasidan meros oladi.
Har bir shakl o'z geometriyasini mustaqil boshqaradi:

```python
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2
```

Ikkalasi ham `Shape` kutilgan joyda ishlatilishi mumkin — **kutilmagan xatti-harakatlarsiz**.
