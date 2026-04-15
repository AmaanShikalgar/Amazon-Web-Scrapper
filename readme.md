# 🛒 Amazon Web Scraper

**Date:** April 2026

---

## Overview

This project is a **dynamic Amazon web scraper** built using Python. The goal was to automate the extraction of product data including **titles, prices, and links** across multiple pages and store the results in a structured CSV format.

The project is divided into two main parts:

1. **Data collection using Selenium**
2. **Data parsing and structuring using BeautifulSoup and Pandas**

---

## Structure

```
├── project.py        # Selenium scraper (collects HTML data)
├── collect.py        # Parses HTML and extracts structured data
├── data/             # Stored raw HTML files
├── data.csv          # Final output dataset
└── requirements.txt  # Dependencies
```

---

## Part 1 — Data Collection (Selenium)

The scraper uses Selenium to:

* Open Amazon search results for a given query
* Iterate across multiple pages
* Extract product containers (`outerHTML`)
* Save each product as an individual `.html` file

**Key decisions:**

* **Page iteration** — enables multi-page scraping instead of a single static page
* **Dynamic query input** — allows scraping different products
* **Controlled delay (`sleep`)** — prevents browser crashes and reduces blocking risk

**Challenges faced:**

* **Invalid session errors** — resolved by proper driver lifecycle management
* **Dynamic content loading** — handled using delays
* **Large HTML size** — managed by storing only product containers

---

## Part 2 — Data Parsing (BeautifulSoup + Pandas)

The parser reads stored HTML files and extracts:

* Product Title
* Price
* Product Link

**Key decisions:**

* **Safe extraction (`None` checks)** — prevents crashes due to missing elements
* **`lxml` parser** — improves performance over default parser
* **Relative → absolute links** — ensures all URLs are usable

**Example logic:**

* Extract `<h2>` → title
* Extract `<span class="a-price-whole">` → price
* Extract `<a class="a-link-normal">` → product link

---

## Output

The script generates a CSV file:

| Title        | Price | Link       |
| ------------ | ----- | ---------- |
| Product Name | ₹999  | Amazon URL |

---

## Key Challenges & Fixes

* **`NoneType` errors**
  → Fixed using conditional checks before accessing elements

* **Slow HTML parsing**
  → Switched to `lxml` parser

* **Broken links**
  → Handled relative URLs properly

* **Single product extraction**
  → Improved selector understanding for scalability

---

## Design Decisions

* **Separate scraper and parser**
  → Keeps responsibilities clean and modular

* **Store raw HTML first**
  → Allows debugging and reprocessing without re-scraping

* **CSV output using Pandas**
  → Makes data ready for analysis

---

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Run scraper:

```bash
python project.py
```

Parse data:

```bash
python collect.py
```

---

## Notes

* Amazon’s HTML structure is dynamic and may change over time
* Some fields may be missing depending on product listings
* This project is for **educational purposes only**

---

## Future Improvements

* Direct scraping to CSV (remove HTML storage step)
* Extract ratings and reviews
* Add pagination optimization using explicit waits
* Improve performance with asynchronous scraping

---

## Author

**Amaan Shikalgar**
