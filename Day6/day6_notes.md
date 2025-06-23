# 🗓️ Day 06 – Random Password Generator 🔐

## 🧩 Challenge:
Generate a secure random password using Python. One version is quick and automatic, and the other lets the user choose character types and counts.

---

## 🧠 Concepts Covered

### 🔹 1. Modules Used
- `random`: Used for selecting random characters and shuffling lists.
- `string`: Provided built-in constants like `ascii_letters`, `digits`, and `punctuation`.

### 🔹 2. Password Generation Logic

#### ✅ Way 1: Quick Generator
- Used `random.choices()` to select 8 random characters from letters, digits, and symbols.
- Combined them using `"".join()` to form a single string.

#### ✅ Way 2: User-Customized Password
- Let the user choose how many **letters**, **symbols**, and **numbers** they want.
- Built the password step-by-step using loops and `random.choice()`.
- Used `random.shuffle()` to mix characters for stronger randomness.
- Used string concatenation to form the final password.

### 🔹 3. Lists and Loops
- Stored different types of characters in lists.
- Appended selected characters using `for` loops.

### 🔹 4. Input and Type Conversion
- Collected numeric input from the user using `input()`, converted to `int` for loop ranges.

---

## 📌 Summary

This challenge helped me understand:
- How to use built-in Python modules to create randomized, secure passwords.
- The difference between a **quick, fixed-length** generator and a **flexible, user-controlled** one.
- How shuffling adds randomness and improves password strength.

Password generation is a fun and practical application of randomness, loops, lists, and user input.
