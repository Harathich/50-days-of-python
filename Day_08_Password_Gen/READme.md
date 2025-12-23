# 🔑 Random Password Picker

A security-focused tool that generates strong, randomized passwords. This project combines string manipulation with random selection to create secure credentials.

## 📄 Description
Weak passwords like "password123" are a security risk. This script generates a complex password containing a mix of Uppercase, Lowercase, Numbers, and Symbols. It also features a "Safety Check" that automatically forces a minimum length of 8 characters if the user requests something too short.

## 🧠 Concepts Learned
This project focused on **String Building** and **Range Loops**:

* **String Concatenation (`+`):**
    * Learned how to merge multiple string pools (letters + numbers + symbols) into one giant dataset.
    * Built the final password character-by-character using `password = password + new_char`.
* **The `random` Module:**
    * Used `random.choice()` to pick a single character from the pool at random.
* **Range Loops (`range()`):**
    * **Key Lesson:** I learned that you cannot loop over an integer directly (e.g., `for i in 10` fails). I must use `range(10)` to tell Python to repeat an action 10 times.
* **Input Validation:**
    * Used an `if/else` block to override the user's input if they requested an unsafe password length (less than 8).

## 💻 How to Run
1. Navigate to the project directory:
   ```bash
   cd 50-days-of-python/Day_08_Password_Gen
