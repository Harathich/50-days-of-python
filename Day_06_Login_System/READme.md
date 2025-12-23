# 🔐 Simple Login System

A fundamental authentication script that simulates a login process. It validates user credentials against stored data using conditional logic.

## 📄 Description
Every app needs a login screen. This project replicates that logic in its simplest form. It asks the user for a username and password, compares them against "hardcoded" correct values, and grants or denies access based on the match. It features specific error messages to tell the user if the username was not found versus if the password was incorrect.

## 🧠 Concepts Learned
This project focused on **Nested Conditionals** and **Logical Flow**:

* **Equality Operators (`==`):**
    * Used to compare the input string exactly against the stored string.
    * *Lesson:* Case sensitivity matters! "Harathich" is not the same as "harathich".
* **Nested `if/else` Statements:**
    * I placed an `if` statement *inside* another `if` statement.
    * This allowed me to create a "gatekeeper" logic: First check the Username. Only if that passes, check the Password.
* **Control Flow:**
    * Learned how to direct the program to different error messages ("Username not found" vs "Incorrect password") depending on where the check failed.

## 💻 How to Run
1. Navigate to the project directory:
   ```bash
   cd 50-days-of-python/Day_06_Login_System
