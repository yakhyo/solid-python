# SOLID Principles

SOLID is an acronym for a set of design principles that were introduced by Robert C. Martin, also known as Uncle Bob.
SOLID principles are a set of design principles that can help developers create maintainable and flexible code.

## Single Responsibility Principle (SRP)

The Single Responsibility Principle states that a class should have only one reason to change. In other words, a class
should have only one responsibility. This principle helps to keep the code organized and easy to maintain.

- Each class or function should have only one responsibility or reason to change.
- Use classes and functions to group related functionality.

## Open/Closed Principle (OCP)

The Open/Closed Principle states that a class should be open for extension but closed for modification. This means that
you should be able to extend the behavior of a class without modifying its source code. This principle helps to ensure
that changes to one part of the codebase don't have unintended consequences elsewhere.

- Classes should be open for extension but closed for modification.
- Use inheritance, polymorphism, and composition to achieve this.

## Liskov Substitution Principle (LSP)

The Liskov Substitution Principle states that subtypes should be substitutable for their base types. In other words, if
you have a method that takes a base type as a parameter, you should be able to pass in any subtype of that base type
without breaking the code. This principle helps to ensure that the code is flexible and can be easily extended.

- Subtypes must be substitutable for their base types.
- Ensure that child classes can be used in place of their parent classes without causing errors or unexpected behavior.

## Interface Segregation Principle (ISP)

The Interface Segregation Principle states that clients should not be forced to depend on interfaces they don't use. In
other words, you should split up large interfaces into smaller, more specific interfaces so that clients can depend on
only what they need. This principle helps to ensure that the code is modular and easy to maintain.

- Clients should not be forced to depend on interfaces they don't use.
- Use multiple small interfaces rather than one large interface.

## Dependency Inversion Principle (DIP)

The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Instead, both
should depend on abstractions. This principle helps to ensure that the code is flexible and can be easily extended.

- Depend on abstractions, not concrete implementations.
- Use dependency injection to provide dependencies to classes and functions.

When using SOLID principles, you can create code that is more maintainable, flexible, and testable. It helps you avoid
tight coupling between components, minimize code duplication, and increase the re-usability of your code.









```
project-name/
    README.md
    LICENSE
    requirements.txt
    setup.py
    project_name/
        __init__.py
        main.py
    tests/
        test_main.py

```

Here's a brief description of each file and directory in this template:

`README.md`: This file contains information about the project, how to use it, and how to contribute to it.
`LICENSE`: This file contains the license under which the project is released. You should choose a license that suits
your
needs and requirements.
`requirements.txt`: This file lists all the dependencies required to run the project. You can use pip to install these
dependencies.
`setup.py`: This file contains the metadata and configuration information for the project. You can use it to install the
project as a Python package.

- `project_name/`: This directory contains the source code for the project.
    - `__init__.py`: This file makes the project_name directory a Python package.
    - `main.py`: This file contains the main logic of the project.
- `tests/`: This directory contains all the unit tests for the project.
    - `test_main.py`: This file contains the unit tests for main.py.

This project template is just a starting point, and you can customize it as per your project requirements. You can add
more directories for additional functionality, documentation, or assets. Additionally, you can include CI/CD
configuration files like `.travis.yml` or `.github/workflows` to automate your testing and deployment processes.