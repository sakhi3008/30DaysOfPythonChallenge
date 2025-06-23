# 🗓️ Day 07 – Word Frequency Counter 📝

## 🧩 Challenge:
Read a text file and count how many times each word appears. Display the result as word → frequency.

---

## 🧠 Concepts Practiced

### 🔹 1. File Handling
- Used `open()` with `'r'` mode to read the contents of a file.
- Used `with` statement for safe file handling — automatically closes the file after reading.

### 🔹 2. Text Cleaning
- Converted all text to lowercase using `.lower()` to ensure consistent word comparison (e.g., `Python` and `python` are counted as the same).

### 🔹 3. String Splitting
- Used `.split()` to break the text into a list of words using spaces as separators.

### 🔹 4. Dictionaries
- Created an empty dictionary to store word counts.
- Used `if-else` logic to either add a new word or update its count.

### 🔹 5. Looping and Display
- Used a `for` loop to go through each word and update counts.
- Displayed each word with its frequency using `print()` and formatted strings.

---

## 📌 Summary

This challenge taught me how to:
- Read and process a text file line by line.
- Count how often each word appears using dictionaries.
- Handle text case sensitivity and word splitting.
- Build a simple but powerful word counter — great for basic text analysis!

This is a useful foundation for more advanced projects like word clouds, sentiment analysis, or building a search engine.
