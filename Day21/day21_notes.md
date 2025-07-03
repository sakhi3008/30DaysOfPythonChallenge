# 🗓️ Day 21 – Web Scraping with `requests` and `BeautifulSoup`

In today's challenge, I learned how to **scrape web data** using two essential Python libraries: `requests` and `BeautifulSoup`. These tools help automate the process of extracting useful data from websites.

---

## 🔹 What is Web Scraping?

Web scraping is the process of automatically extracting information from websites. It involves sending HTTP requests to a website and parsing the HTML to retrieve the required content.

---

## 🔹 `requests` Library

The `requests` library is used to send HTTP requests in Python.

### Key Methods:

* `requests.get(url)`: Sends a GET request to the given URL.
* `response.text`: Returns the content of the response in Unicode.
* `response.status_code`: Returns the HTTP status code (e.g., 200 for success).

**Example:**

```python
import requests
response = requests.get("https://example.com")
print(response.text)
```

---

## 🔹 `BeautifulSoup` Library

`BeautifulSoup` is used for parsing HTML and XML documents. It allows you to navigate the HTML tree easily and extract data.

### Key Concepts:

* `soup = BeautifulSoup(html, "html.parser")`: Create a BeautifulSoup object.
* `soup.find(tag)`: Find the first instance of a tag.
* `soup.find_all(tag)`: Find all instances of a tag.
* `.get_text()`: Extract text from an HTML tag.

**Example:**

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("h3")
```

---

## 🎯 Challenge – Scrape Headlines from a News Site

### Objective:

Scrape the top headlines from [The Hindu](https://www.thehindu.com/) homepage using `requests` and `BeautifulSoup`.

### Steps Taken:

1. Sent a GET request to `https://www.thehindu.com/` using `requests.get()`.
2. Parsed the HTML response using `BeautifulSoup`.
3. Found all `<h3>` tags, which typically contain the headlines.
4. Printed the top 20 headlines with enumeration.

### What I Learned:

* How to fetch a webpage's HTML content using `requests`.
* How to parse and navigate HTML content using `BeautifulSoup`.
* How to extract and clean text data from HTML tags.

---

## 🤔 Why This Matters:

Web scraping is an essential skill for data analysts, journalists, and developers who need to collect real-time data from the web. Today’s exercise taught me how to automate content extraction, which can be applied to:

* News monitoring
* Price tracking
* Job listings aggregation
* Research and analysis tasks

---

Let me know if you want the Day 22 notes next!
