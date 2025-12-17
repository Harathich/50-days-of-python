# ⏱️ Seconds to Time Converter

A logic-based Python script that takes a raw number of seconds (e.g., 3665) and converts it into a human-readable format of Hours, Minutes, and Seconds.

## 📄 Description
We often deal with time in raw seconds in programming (timestamps, duration logs), but humans read time in `HH:MM:SS`. This program uses mathematical logic to break down a large integer into smaller units of time without using any external libraries.

## 🧠 Concepts Learned
This project was a deep dive into **Arithmetic Operators** and logical flow:

* **Floor Division (`//`):**
    * I learned that normal division (`/`) gives a decimal (float).
    * To get the "whole" number of hours or minutes, I had to use Floor Division (e.g., `3665 // 3600` gives `1`, not `1.018`).
* **The Modulo Operator (`%`):**
    * **Crucial Lesson:** This operator returns the *remainder* of a division.
    * I used this to "catch" the leftover seconds that didn't fit into a full hour or minute.
    * *Formula:* `remaining_seconds = total_seconds % 3600`.
* **String Formatting (f-strings):**
    * Learned how to embed the calculated variables directly into a print statement for a clean output like `1 Hours, 1 Minutes`.

## 💻 How to Run
1. Navigate to the project directory:
   ```bash
   cd 50-days-of-python/Day_03_Seconds_Converter
