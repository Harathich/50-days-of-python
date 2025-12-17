# 🎂 Age Calculator

A simple yet essential Python script that calculates a user's exact age based on their birth year. This project focuses on handling user input, performing arithmetic operations, and managing data types.

## 📄 Description
This program asks the user for their birth year (and optionally their birth month) to calculate their current age. It handles the logic of converting text input into numbers to perform mathematical subtraction against the current year.

## 🧠 Concepts Learned
Building this project helped reinforce the following Python fundamentals:

* **Input Handling (`input()`):** * Learned how to capture data from the user via the console.
* **Type Casting (`int()` vs `str`):** * **Crucial Lesson:** The `input()` function returns a *string* by default. I learned that I must convert this string into an *integer* using `int()` before performing any math, otherwise the program crashes.
* **Arithmetic Operators:**
    * Used subtraction (`-`) to determine the age gap.
* **Conditional Logic (`if/else`):**
    * *implied:* Used to check if the user's birthday has already passed this year to adjust the age calculation (e.g., subtracting 1 if the current month < birth month).
* **Dynamic Variables:**
    * Storing values like `current_year` in variables rather than hardcoding them everywhere makes the code easier to update.

## 💻 How to Run
1. Ensure you have Python installed.
2. Navigate to the project directory:
   ```bash
   cd 100-days-of-python/Day_02_Age_Calculator
