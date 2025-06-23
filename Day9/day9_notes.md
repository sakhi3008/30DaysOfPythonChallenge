# 🗓️ Day 09 – Inheritance & Polymorphism in OOP ⚙️⚡

## 🧠 Key OOP Concepts

### 🔹 Inheritance
Inheritance lets one class (**child**) reuse the code from another class (**parent**).  
It helps avoid repetition and promotes code reusability.

- `ElectricCar` inherits from `Car`
- It automatically gets `brand`, `model`, `color`, and methods from the `Car` class

### 🔹 `super()` Keyword
- Used to call the **parent class's constructor** or methods from the child class.
- `super().__init__()` lets `ElectricCar` access and reuse `Car`'s constructor logic.

### 🔹 Polymorphism (Method Overriding)
Polymorphism means "**many forms**". In Python OOP, it often refers to **overriding a method** in the child class to behave differently.

- `ElectricCar` overrides the `display()` method from `Car`
- The new version includes **battery capacity** info, specific to electric cars

---

## ✅ What I Did in Code

1. Created a `Car` class with basic attributes and a `display()` method.
2. Made a subclass `ElectricCar` that:
   - Inherited everything from `Car`
   - Added a new attribute: `battery_capacity`
   - Overrode the `display()` method to show battery info
3. Created an `ElectricCar` object and used `display()` to show full details.

---

## 📌 Summary

This challenge helped me understand:
- How to **extend** an existing class using inheritance
- How to **reuse and customize** methods using `super()` and method overriding
- The power of polymorphism to make classes more flexible and specific

OOP becomes even more powerful when we use inheritance and polymorphism to handle complex scenarios efficiently.
