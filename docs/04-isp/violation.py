"""Interface Segregation Principle -- Violation.

A single fat `Worker` interface forces every implementor to provide
work(), eat(), and sleep() — even when some of those make no sense
(e.g. a Robot doesn't eat or sleep).
"""

from abc import ABC, abstractmethod


class Worker(ABC):
    """Fat interface — clients are forced to depend on methods they don't use."""

    @abstractmethod
    def work(self) -> str: ...

    @abstractmethod
    def eat(self) -> str: ...

    @abstractmethod
    def sleep(self) -> str: ...


class Human(Worker):
    def __init__(self, name: str) -> None:
        self.name = name

    def work(self) -> str:
        return f"{self.name} is working"

    def eat(self) -> str:
        return f"{self.name} is eating"

    def sleep(self) -> str:
        return f"{self.name} is sleeping"


class Robot(Worker):
    """Robots don't eat or sleep, yet the interface forces stub methods."""

    def __init__(self, model: str) -> None:
        self.model = model

    def work(self) -> str:
        return f"Robot {self.model} is working"

    def eat(self) -> str:
        raise NotImplementedError("Robots don't eat")

    def sleep(self) -> str:
        raise NotImplementedError("Robots don't sleep")


if __name__ == "__main__":
    alice = Human("Alice")
    print(alice.work())
    print(alice.eat())

    t800 = Robot("T-800")
    print(t800.work())
    print(t800.eat())  # raises NotImplementedError!
