"""
The **Interface Segregation Principle (ISP)** is a principle in
object-oriented programming that states that no client should be
forced to depend on methods it does not use. In other words, a
class should not have to implement methods that it does not need or
use, and interfaces should be designed to be as small and cohesive as possible.

The ISP is one of the five SOLID principles of object-oriented design,
which aim to create more maintainable and flexible software systems.
The ISP is important because it promotes code that is more modular,
flexible, and extensible, which makes it easier to understand, test, and modify.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius**2)

    def perimeter(self):
        return 2 * 3.14 * self.radius


class VolumeCalculator:
    def volume(self, shapes):
        total_volume = 0
        for shape in shapes:
            if isinstance(shape, Shape):
                total_volume += shape.area() * shape.perimeter()
        return total_volume


"""
In this example, we have a base interface `Shape` with two abstract 
methods: `area()` and `perimeter()`. We then have two concrete classes 
`Rectangle` and `Circle` that implement the Shape interface.

We also have a `VolumeCalculator` class that calculates the total 
volume of a list of shapes. The `volume()` method takes a list of
shapes as input, and iterates over them, calculating the area and
perimeter of each shape and adding them together.

By using the ISP, we have separated the Shape interface into two separate
methods (`area() `and` perimeter()`), which allows us to implement only 
the methods that are relevant to each shape. This means that a `Rectangle`
object does not need to implement a `perimeter()` method that is not relevant
to it, and a `Circle` object does not need to implement an `area()` method 
that is not relevant to it.

This also means that we can pass any object that implements the `Shape` 
interface to the `VolumeCalculator` class, without worrying about whether
it has implemented methods that are not relevant to it. This makes our 
code more flexible and extensible, and easier to maintain and test.
"""
