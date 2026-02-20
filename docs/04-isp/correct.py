"""Interface Segregation Principle -- Correct.

The fat Worker interface is split into small, focused interfaces.
Each class implements only the interfaces that are relevant to it.
"""

from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self) -> str: ...


class Eatable(ABC):
    @abstractmethod
    def eat(self) -> str: ...


class Sleepable(ABC):
    @abstractmethod
    def sleep(self) -> str: ...


class Human(Workable, Eatable, Sleepable):
    def __init__(self, name: str) -> None:
        self.name = name

    def work(self) -> str:
        return f"{self.name} is working"

    def eat(self) -> str:
        return f"{self.name} is eating"

    def sleep(self) -> str:
        return f"{self.name} is sleeping"


class Robot(Workable):
    """Implements only Workable — no forced eat() or sleep() stubs."""

    def __init__(self, model: str) -> None:
        self.model = model

    def work(self) -> str:
        return f"Robot {self.model} is working"


def assign_task(worker: Workable) -> None:
    print(worker.work())


if __name__ == "__main__":
    alice = Human("Alice")
    assign_task(alice)
    print(alice.eat())
    print(alice.sleep())

    t800 = Robot("T-800")
    assign_task(t800)
