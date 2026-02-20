---
layout: default
title: "Interface Segregation (UZ)"
nav_exclude: true
permalink: /uz/04-isp/
---

{: .note }
> **Til:** [English]({{ site.baseurl }}/04-isp/) | **O'zbek**

# Interface Segregation Principle (ISP)

> Klientlar o'zlari **ishlatmaydigan** interfeyslarga bog'liq bo'lmasligi kerak.

Katta, bir butun interfeyslarni **kichik va aniq** interfeyslarga ajratish lozim.
Har bir klass faqat o'ziga tegishli metodlarni implement qilishi kerak.

## Diagramma

<p align="center">
  <img src="{{ site.baseurl }}/assets/04-isp.png" width="700" alt="ISP klass diagrammasi" style="border-radius: 12px;" />
</p>

## Noto'g'ri yondashuv

[`violation.py`](violation.py) dagi bitta katta `Worker` interfeysi uni implement qiluvchi barcha klasslarni `work()`, `eat()` va `sleep()` metodlarini yozishga majbur qiladi:

```python
class Worker(ABC):
    @abstractmethod
    def work(self) -> str: ...

    @abstractmethod
    def eat(self) -> str: ...

    @abstractmethod
    def sleep(self) -> str: ...
```

`Robot` ovqatlanmaydi va uxlamaydi, lekin interfeys uni bu metodlarni yozishga majbur qiladi:

```python
class Robot(Worker):
    def eat(self) -> str:
        raise NotImplementedError("Robots don't eat")

    def sleep(self) -> str:
        raise NotImplementedError("Robots don't sleep")
```

## To'g'ri yondashuv

[`correct.py`](correct.py) da esa katta interfeys uchta kichik interfeysga ajratilgan:

| Interfeys | Metod |
|-----------|-------|
| `Workable` | `work()` |
| `Eatable` | `eat()` |
| `Sleepable` | `sleep()` |

Har bir klass **faqat o'ziga kerakli** interfeyslarni implement qiladi:

```python
class Human(Workable, Eatable, Sleepable):
    ...

class Robot(Workable):  # eat() va sleep() talab qilinmaydi
    def work(self) -> str:
        return f"Robot {self.model} is working"
```

Faqat ishchi kerak bo'lgan funksiya `Workable` interfeysini qabul qiladi — keraksiz `eat()` yoki `sleep()` metodlariga bog'liq bo'lmaydi.
