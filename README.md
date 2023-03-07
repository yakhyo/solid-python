# SOLID Principles

SOLID is an acronym for a set of design principles that were introduced by Robert C. Martin, also known as Uncle Bob.
SOLID principles are a set of design principles that can help developers create maintainable and flexible code.

## Table of Contents

- [Single Responsibility Principle (SRP)](solid_python/srp)
- [Open/Closed Principle (OCP)](solid_python/ocp)
- [Liskov Substitution Principle (LSP)](solid_python/lsp)
- [Interface Segregation Principle (ISP)](solid_python/isp)
- [Dependency Inversion Principle (DIP)](solid_python/dip)

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
