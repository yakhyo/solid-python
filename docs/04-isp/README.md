---
layout: default
title: "Interface Segregation"
nav_order: 5
permalink: /04-isp/
---

{: .note }
> **Language:** **English** | [O'zbek]({{ site.baseurl }}/uz/04-isp/)

# Interface Segregation Principle (ISP)

> Clients should not be forced to depend on interfaces they do not use.

Large, monolithic interfaces should be split into **smaller, focused** ones.
A class should only implement the methods that are relevant to its behavior.

## Diagram

<p align="center">
  <img src="{{ site.baseurl }}/assets/04-isp.png" width="700" alt="ISP class diagram" style="border-radius: 12px;" />
</p>

## Violation

In [`violation.py`](violation.py) a fat `Worker` interface forces every implementor to provide `work()`, `eat()`, and `sleep()`:

```python
class Worker(ABC):
    @abstractmethod
    def work(self) -> str: ...

    @abstractmethod
    def eat(self) -> str: ...

    @abstractmethod
    def sleep(self) -> str: ...
```

A `Robot` has no concept of eating or sleeping, yet it is forced to implement those methods:

```python
class Robot(Worker):
    def eat(self) -> str:
        raise NotImplementedError("Robots don't eat")

    def sleep(self) -> str:
        raise NotImplementedError("Robots don't sleep")
```

## Correct

In [`correct.py`](correct.py) the fat interface is split into three focused interfaces:

| Interface | Method |
|-----------|--------|
| `Workable` | `work()` |
| `Eatable` | `eat()` |
| `Sleepable` | `sleep()` |

Each class implements **only** what it needs:

```python
class Human(Workable, Eatable, Sleepable):
    ...

class Robot(Workable):  # no eat() or sleep() required
    def work(self) -> str:
        return f"Robot {self.model} is working"
```

A function that only needs workers accepts `Workable` — it does not pull in unused `eat()` or `sleep()` contracts.
