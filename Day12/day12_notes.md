# 🗓️ Day 12 – re module, pattern matching and regex challenge

In this challenge, I explored Python’s `re` module, which is used for working with **regular expressions (regex)** — a powerful tool for pattern matching in strings. It allows us to search, validate, or manipulate text efficiently, making it useful in many real-world scenarios such as input validation, data scraping, or string filtering.

---

### 🔹 What is the `re` Module?

The `re` module is Python's standard library for performing operations with regular expressions. It provides various functions and methods to match patterns in strings.

---

### 🔹 Useful `re` Functions:

- **`re.match()`**  
  Checks if the **pattern matches at the beginning** of a string.

- **`re.search()`**  
  Searches the **entire string** for the first match of the pattern.

- **`re.findall()`**  
  Returns **all non-overlapping matches** of the pattern in the string as a list.

- **`re.sub()`**  
  Used to **substitute** occurrences of a pattern with a replacement string.

---

### 🔹 Regex Pattern Components Used

To validate Gmail addresses, a pattern like `^[a-zA-Z0-9._]+@gmail\.com$` is used. Here's the breakdown:

- `^` – Anchors the pattern to the **start** of the string  
- `[a-zA-Z0-9._]+` – Allows letters (upper/lower), digits, dot (.), and underscore (_) **one or more times**  
- `@gmail\.com` – Ensures the domain is exactly `@gmail.com`  
- `$` – Anchors the pattern to the **end** of the string

This pattern ensures only Gmail addresses are matched and avoids other domains like `yahoo.com`.

---

### 🎯 Challenge – Validate Gmail Addresses Using Regex

In this challenge, I:
- Wrote a function using `re.match()` to validate if the email ends with `@gmail.com` and has only allowed characters before it.
- Applied this validation across a list of emails.
- Printed whether each email is valid or not.

---

This task helped me understand how to:
- Use the `re` module for pattern matching
- Build basic regex patterns
- Validate real-world input like email addresses

Regular expressions are powerful and widely used in tasks such as data cleaning, parsing logs, scraping, and form validation — and mastering them is crucial for any developer or data professional.

---

### 📚 Additional Resource

For more regex patterns, examples, and good practices, visit:  
🔗 [https://regex101.com](https://regex101.com) – A great interactive site to test and understand regular expressions.
