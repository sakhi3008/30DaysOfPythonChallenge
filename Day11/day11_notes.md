# 🗓️ Day 11 – Datetime module, formatting, time differences and challenges

In this challenge, I explored Python’s built-in `datetime` module, which is widely used for working with dates and times. It allows us to handle user input in date format, perform time-based calculations, and display time-related information in readable formats — all essential for building time-sensitive applications.

---

### 🔹 strptime (String ➝ Datetime)

`strptime()` stands for **string parse time**. It is used to convert a string (like user input) into a `datetime` object by specifying the format of the input string. This is useful when accepting dates from users or reading date data from files.

---

### 🔹 strftime (Datetime ➝ String)

`strftime()` stands for **string format time**. It formats a `datetime` object into a readable string based on the format we choose. This is especially helpful when we need to display dates in a specific style (e.g., "DD-MM-YYYY").

---

### 🔹 timedelta

When two datetime objects are subtracted, Python returns a `timedelta` object, which represents the duration between the two dates. Using `.days` on that object gives the difference in days. If the order of dates is uncertain, using `abs()` ensures a positive result.

---

### 🎯 Challenge – Calculate the days between two dates

In this challenge, I:
- Took two date inputs in `"DD-MM-YYYY"` format.
- Converted those strings into `datetime` objects using `strptime()`.
- Calculated the difference using subtraction and extracted the number of days using `.days`.
- Applied `abs()` to make sure the day difference is always positive.
- Displayed the result in a clean, user-friendly way.

This task helped reinforce the concepts of date parsing, formatting, and working with time differences — which are key in many practical applications like logs, calendars, deadlines, and scheduling systems.
