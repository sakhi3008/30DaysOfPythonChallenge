# 🗓️ Day 03 – Inventory System using Dictionary

## 📌 Challenge
Create an inventory system that tracks items and their quantities using a dictionary.

---

## 🧠 Concepts Used

### 🔹 1. Dictionary Creation and Manipulation
- I used a dictionary named `inventory` to store items as keys and their quantities as values.
- I added items manually using `inventory['item'] = quantity`.
- I updated item quantities by directly modifying values (`inventory['item'] += value`).
- I removed items using the `del` statement and `pop()` method.

### 🔹 2. `update()` Method
- I used `inventory.update({...})` to add or update multiple items efficiently.
- This helped avoid repetitive assignments.

### 🔹 3. Tuples
- I used a tuple to store an item and its quantity temporarily, then unpacked it into the dictionary using `update()`.

### 🔹 4. Sets for Duplicate Checking
- I created a set of existing item names using `set(inventory.keys())`.
- Then, I checked whether an item was already present before updating it. This prevented duplicates.

### 🔹 5. Loops and `items()` Method
- I used a `for` loop with `.items()` to display each item and its quantity neatly.
- Helped in printing the entire inventory in a readable way.

### 🔹 6. Functions
- I wrote separate functions to:
  - Display the inventory
  - Add an item
  - Update an item
  - Remove an item
- This made the code cleaner, modular, and easier to understand.

### 🔹 7. User Interaction (Input)
- I created an interactive menu using `input()` to take choices from the user.
- The program repeatedly asked the user for actions until they chose to exit.

### 🔹 8. Loops and Control Flow
- I used a `while True` loop to keep the program running.
- Inside it, I used `if-elif-else` statements to perform different actions based on user input.
- Exiting the loop with `break` when the user chooses to quit.

---

## ✅ What I Learned

- How to use dictionaries to build real-life systems like inventory tracking.
- How to manage dictionary data using update, add, and delete operations.
- How to combine functions, loops, and user input to create an interactive program.
- The value of using sets and conditionals to handle duplicate entries.
- Structured thinking and modular coding by separating logic into functions.

