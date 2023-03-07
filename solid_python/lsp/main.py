"""
The LSP is important because it ensures that code is robust and extensible. It allows us to write code that is generic
and reusable, because we can create base classes that define common behavior, and then create derived classes that
specialize that behavior. The LSP also makes it easier to test and debug code, because we can substitute objects with
mock objects in our tests, without affecting the correctness of the program.

Here's an example code for the Liskov Substitution Principle (LSP) in Python:
"""


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


"""
In this example, we have a base class `Shape` that has a method `area`. We also have two derived classes, `Rectangle`
and `Square`, that inherit from `Shape` and implement the `area` method.

The `Rectangle` class represents a rectangle with a given width and height. It overrides the area method to calculate
the `area` of the rectangle based on its width and height.

The `Square` class represents a square with a given side length. It also overrides the `area` method to calculate the
area of the square based on its side length.

The LSP states that objects of a derived class should be able to replace objects of a base class without affecting the
correctness of the program. In this example, the `Square` class can be substituted for the `Rectangle` class in any code
that expects a `Shape` object, without affecting the correctness of the program. However, this is not always the case,
as we'll see below.
"""


def print_shape_area(shape):
    print(f"The area of the shape is {shape.area()}")


rectangle = Rectangle(5, 10)
square = Square(5)

print_shape_area(rectangle)
print_shape_area(square)  # this will produce an incorrect result

"""
In this example, we have a function `print_shape_area` that takes a `Shape` object and prints its area. We create a
`Rectangle` object with a width of 5 and a height of 10, and a Square object with a side length of 5. We pass both
objects to the print_shape_area function.

The `print_shape_area` function works correctly for the `Rectangle` object, but it produces an incorrect result for the
`Square` object. This is because the `Square` class violates the LSP, as it does not behave like a rectangle. A square
has all sides equal, whereas a rectangle has opposite sides equal. Therefore, when we pass a `Square` object to a
function that expects a `Rectangle` object, the function will behave incorrectly.

To apply the LSP, we should ensure that derived classes behave like their base class. In this example, we can fix the
`Square` class by inheriting from the `Rectangle` class, and ensuring that its width and height are always equal to its
side length:
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return super().area()


"""
In this updated code, the `Square` class inherits from the `Rectangle` class, and its width and height are always equal
to its side length. The `Square` class now behaves like a rectangle, and it can be substituted for a `Rectangle` object
in any code that expects a `Shape` object, without affecting the correctness of the program.
"""
