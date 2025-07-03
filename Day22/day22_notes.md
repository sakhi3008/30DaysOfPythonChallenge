# 🗓️ Day 22 – Building a CLI Tool with `argparse`

In today’s challenge, I explored the powerful `argparse` module in Python to create a **Command-Line Interface (CLI) tool**. The project was a **temperature converter** that allows users to convert values between Celsius, Fahrenheit, and Kelvin.

---

## 🔹 What is a CLI Tool?

A CLI (Command-Line Interface) tool allows users to interact with a program by typing commands into a terminal or command prompt. Python provides the `argparse` module to help parse command-line arguments easily and securely.

---

## 🔹 What is `argparse`?

`argparse` is a built-in Python module used to handle command-line arguments passed to a script. It provides:

* A way to define arguments
* Automatic help message generation
* Argument validation and type checking

---

## 📆 Key Concepts

### 1. **ArgumentParser()**

This is the main entry point. You create a parser object that holds all information for parsing arguments.

```python
parser = argparse.ArgumentParser(description="Description of your CLI tool")
```

### 2. **add\_argument()**

Used to define what arguments the program expects.

```python
parser.add_argument("value", type=float, help="Temperature to convert")
```

You can also specify:

* `type`: The expected data type
* `help`: Description of the argument
* `choices`: Limit acceptable inputs (e.g., `choices=["C", "F", "K"]`)

### 3. **parse\_args()**

Parses the command-line arguments and returns a namespace.

```python
args = parser.parse_args()
```

Access your inputs using `args.argument_name`.

---

## 📊 Challenge – Temperature Converter CLI Tool

### 🔹 What I Built:

* A temperature converter that accepts input in Celsius, Fahrenheit, or Kelvin and converts it to the desired unit.
* Example usage:

  ```bash
  python temp_converter.py 100 C F
  ```

  This converts 100°C to Fahrenheit.

### 🔎 Key Features:

* Uses `argparse` to take 3 arguments: value, from\_unit, to\_unit
* Converts temperature through Celsius as an intermediate
* Handles invalid inputs with `ValueError`
* Prints output with proper formatting and rounding

### 🔧 Benefits of This Approach:

* Reusable for any temperature input
* Provides a professional CLI experience
* Clear error handling and input restrictions

---

## 🚀 Why This Matters

Understanding how to build CLI tools using `argparse` opens the door to creating:

* Automation scripts
* File processors
* System utilities
* Lightweight developer tools

Today, I gained hands-on experience converting a typical Python function into a fully functional command-line application!
