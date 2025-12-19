# 🆔 Random Username Generator

A fun, beginner-friendly Python script that creates unique usernames by "remixing" your first and last name with a random number.

## 📄 Description
Creating unique usernames for websites or games can be hard. This program automates the process by taking the first few letters of a user's first and last name and combining them with a randomly generated 2-digit number.

## 🧠 Concepts Learned
This project helped me master **String Manipulation** and **Modules**:

* **String Slicing (`[0:3]`):**
    * I learned how to extract specific parts of a text string.
    * Used `first_name[0:3]` to grab just the first three letters (e.g., "Michael" -> "Mic").
* **The `random` Module:**
    * Learned how to import Python's built-in library `import random`.
    * Used `random.randint(1, 99)` to generate unpredictable numbers for uniqueness.
* **Type Casting (`str()`):**
    * **Key Lesson:** Python cannot combine text (string) and numbers (integers) directly.
    * I had to explicitly convert the random number into a string using `str(randomint)` before combining it with the names.
* **String Concatenation (`+`):**
    * Joined multiple strings together to form the final username.

## 💻 How to Run
1. Navigate to the project directory:
   ```bash
   cd 50-days-of-python/Day_04_Username_Generator
