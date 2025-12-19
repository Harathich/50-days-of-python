# ⚖️ Odd or Even Checker

A fundamental Python script that determines whether a user-submitted number is Odd or Even. This project includes specific logic to handle the edge case of Zero.

## 📄 Description
Sorting numbers into "Odd" or "Even" is one of the most common logic checks in programming. This script takes an integer input and uses the **Modulo Operator** to check for a remainder when divided by 2. It also features a custom message if the user inputs `0`.

## 🧠 Concepts Learned
This project focused on **Control Flow** and **Mathematical Logic**:

* **The Modulo Operator (`%`):**
    * **Key Lesson:** I learned that `%` gives the remainder.
    * `number % 2 == 0` means the number is perfectly divisible by 2 (Even).
* **Conditional Statements (`if / else`):**
    * Used to create a "fork in the road" for the code logic.
* **Nested Conditionals:**
    * I placed an `if` statement *inside* another `if` statement to specifically check if the even number was `0`.
* **Equality Operators (`==`):**
    * Learned the difference between assigning a value (`=`) and comparing values (`==`).

## 💻 How to Run
1. Navigate to the project directory:
   ```bash
   cd 50-days-of-python/Day_05_Odd_Even
