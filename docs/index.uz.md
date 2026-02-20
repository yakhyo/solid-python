---
layout: default
title: Bosh sahifa
nav_exclude: true
permalink: /uz/
---

{: .note }
> **Til:** [English]({{ site.baseurl }}/) | **O'zbek**

<p align="center">
  <img src="{{ site.baseurl }}/assets/banner.png" alt="Python'da SOLID Tamoyillari" />
</p>

# Python'da SOLID Tamoyillari

SOLID — Robert C. Martin (Uncle Bob) tomonidan taqdim etilgan beshta dizayn tamoyilining qisqartmasi.
Bu tamoyillar dasturchilarga oson kengaytiriladigan, tushunarli va qo'llab-quvvatlanadigan kod yozishga yordam beradi.

Har bir tamoyil **noto'g'ri yondashuv** va **to'g'ri yechim** ko'rinishida, UML klass diagrammasi bilan birga ko'rsatilgan.

## Tamoyillar

| # | Tamoyil | Tavsif |
|---|---------|--------|
| **S** | [Single Responsibility (SRP)]({{ site.baseurl }}/uz/01-srp/) | Har bir klass faqat bitta vazifaga ega bo'lishi kerak |
| **O** | [Open/Closed (OCP)]({{ site.baseurl }}/uz/02-ocp/) | Kengaytirish uchun ochiq, o'zgartirish uchun yopiq |
| **L** | [Liskov Substitution (LSP)]({{ site.baseurl }}/uz/03-lsp/) | Quyi turlar (subtype'lar) asosiy turlar (base type'lar) o'rnida ishlatilishi mumkin bo'lishi kerak |
| **I** | [Interface Segregation (ISP)]({{ site.baseurl }}/uz/04-isp/) | Klientlar o'zlariga kerak bo'lmagan interfeyslarga bog'liq bo'lmasligi kerak |
| **D** | [Dependency Inversion (DIP)]({{ site.baseurl }}/uz/05-dip/) | Konkret klasslarga emas, abstraktsiyalarga bog'laning |

## Misollarni ishga tushirish

Har bir fayl mustaqil skript hisoblanadi. Istalgan misolni to'g'ridan-to'g'ri ishga tushiring:

```bash
python docs/01-srp/violation.py
python docs/01-srp/correct.py
```

**Talablar:** Python 3.10+, tashqi kutubxonalar talab qilinmaydi.

## Litsenziya

[MIT]({{ site.repo_url }}/blob/main/LICENSE) — Yaxyo Valixo'jayev
