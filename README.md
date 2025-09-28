# PytestPythonDemo – Amazon Automation Framework 🚀

---

## 🗑 Introduction

This project is an **automated test framework for Amazon India** using **Playwright with Python** and follows the **Page Object Model (POM)** design pattern.
It demonstrates searching products, validating details, and adding affordable products to the cart.

---

## 📂 Project Structure

```
PytestPythonDemo/
└── PythonProject/
    ├── 📁 data/                  # Test data files
    ├── 📁 pages/                 # Page Object Model classes
    │    ├── 🗑 home_page.py
    │    ├── 🗑 search_results_page.py
    │    └── 🗑 product_page.py
    ├── 📁 test-results/          # Pytest trace viewer files
    ├── 📁 tests/                 # Test scripts
    │    └── 🗑 test_amazon.py
    ├── 📁 utils/                 # Helper functions
    │    └── 🗑 helpers.py
    ├── 🗑 conftest.py            # Pytest fixtures (optional)
    └── 🗑 report.html            # Sample HTML test report
```

---

## ✨ Key Features

* Implements **Page Object Model (POM)** for maintainable code.
* Reusable **utilities** like `parse_price()`.
* Stops after adding the **first affordable product** (≤ ₹50,000) to the cart.
* Generates **HTML reports** for results.
* Generate Trace files for Visual debug tool for Playwright; inspect steps, DOM, screenshots, and network requests.

---

## ⚡ Pre-requisites

* Python >= 3.13.7
* Playwright >= 1.55.0
* pytest >= 8.4.2
* Google Chrome / Chromium installed

---

## 🏃 Running the Tests

### 🖥️ Using PyCharm

* Open `PythonProject` in PyCharm.
* Right-click any test file (e.g., `test_amazon.py`) → Run.

### 💻 Using Command Line

```bash
# From PythonProject root
pytest tests/test_amazon.py --tracing on --html=report.html --headed
```

* `--tracing on` → generates the tracer zip file.
* `--headed` → runs the browser visibly. Remove for headless execution.
* `--html=report.html` → generates an HTML report.

---

## 📊 Reporting

* Test reports are generated in `test-results/` folder.
* `report.html` provides a **summary of test execution**.

---

## 🔍 Trace Viewer

* Playwright traces can be **recorded and viewed** for debugging.
* Use [https://trace.playwright.dev/](https://trace.playwright.dev/) to open and view the trace file.

---

## 🔄 How it Works

**Workflow Diagram:**

```
+---------------------------+
|       🏠 Amazon Home Page       |
+---------------------------+
             |
             v
+---------------------------+
|           🔍 Search            |
+---------------------------+
             |
             v
+---------------------------+
|       📄 Search Results       |
+---------------------------+
             |
             v
+---------------------------+
|        📦 Product Page         |
+---------------------------+
             |
             v
+---------------------------+
|        🛒 Add to Cart         |
+---------------------------+
             |
             v
+---------------------------+
|           💳 Checkout          |
+---------------------------+
```

---

## 📚 References

* [Playwright Python Documentation](https://playwright.dev/python/docs/intro)
* [Python POM Design Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

---

## 👤 Author

**Hariharamanikandan** – Automation Enthusiast

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github&style=flat-square)](https://github.com/hari16292)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/hariharamanikandan)

