# 🗓️ Day 10 – Exception Handling in Python ⚠️

## 🧠 Key Concepts

### 🔹 `try-except`
- Used to **catch errors** that may occur during program execution.
- Code inside `try` is executed; if any error occurs, control jumps to `except`.

### 🔹 Specific Exceptions
- Catching general errors works, but catching **specific errors** (like `FileNotFoundError`, `ValueError`) is better practice.
- It helps to **identify and handle** only the expected issues.

### 🔹 `finally` Clause
- Runs **no matter what happens** – whether an error occurred or not.
- Used for cleanup tasks like closing files or displaying a completion message.

---

## ✅ What I Did in Code

1. **Opened a file** using `with open()` safely inside a `try` block.
2. **Read each line**, stripped extra spaces, and tried converting it to a number.
3. Used a **nested `try-except`** block:
   - If the conversion failed (non-numeric line), printed a skip message.
4. Summed only the valid numbers.
5. If the file path was wrong or missing, caught the `FileNotFoundError`.
6. Used `finally` to show a message that the execution is complete — even if something went wrong.

---

## 📌 Summary

This challenge helped me learn how to:
- Gracefully **handle runtime errors**
- Keep the program running even with invalid data
- Use `try`, `except`, and `finally` to write **robust and safe Python code**

It’s an essential skill for building real-world applications that can handle user mistakes, missing files, or bad input without crashing.
