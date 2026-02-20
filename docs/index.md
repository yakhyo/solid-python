---
layout: default
title: Home
nav_order: 1
permalink: /
---

{: .note }
> **Language:** **English** | [O'zbek]({{ site.baseurl }}/uz/)

<p align="center">
  <img src="{{ site.baseurl }}/assets/banner.png" alt="SOLID Principles in Python" />
</p>

# SOLID Principles in Python

SOLID is an acronym for five design principles introduced by Robert C. Martin (Uncle Bob).
They guide developers toward code that is maintainable, flexible, and easy to extend.

Each principle is demonstrated with a **violation** (what goes wrong) and a **correct** implementation (how to fix it), accompanied by a UML class diagram.

## Principles

| # | Principle | Description |
|---|-----------|-------------|
| **S** | [Single Responsibility (SRP)]({{ site.baseurl }}/01-srp/) | A class should have only one reason to change |
| **O** | [Open/Closed (OCP)]({{ site.baseurl }}/02-ocp/) | Open for extension, closed for modification |
| **L** | [Liskov Substitution (LSP)]({{ site.baseurl }}/03-lsp/) | Subtypes must be substitutable for their base types |
| **I** | [Interface Segregation (ISP)]({{ site.baseurl }}/04-isp/) | Clients should not depend on interfaces they don't use |
| **D** | [Dependency Inversion (DIP)]({{ site.baseurl }}/05-dip/) | Depend on abstractions, not concrete implementations |

## Running the Examples

Each file is a standalone script. Run any example directly:

```bash
python docs/01-srp/violation.py
python docs/01-srp/correct.py
```

**Requirements:** Python 3.10+, no external dependencies.

## License

[MIT]({{ site.repo_url }}/blob/main/LICENSE) — Yakhyokhuja Valikhujaev
