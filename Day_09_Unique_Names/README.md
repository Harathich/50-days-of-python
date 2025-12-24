# 👥 Unique Name Checker

A data-cleaning script that removes duplicate entries from a list of names. This project introduces Python's **Set** data structure, which is designed to handle unique values automatically.

## 📄 Description
In real-world data (like event registrations or survey responses), duplicates are common. This program allows users to input a continuous stream of names. Once finished, it processes the list to report two key metrics: the total number of entries and the actual number of *unique* individuals, effectively filtering out any double-entries.

## 🧠 Concepts Learned
This project focused on **Data Structures** and **Type Casting**:

* **Sets (`set()`):**
    * **Key Lesson:** I learned that unlike Lists, a **Set** cannot hold duplicate items.
    * Converting a List to a Set is the fastest way to "clean" data and remove duplicates.
* **List vs. Set:**
    * *List:* Ordered, allows duplicates (`['Bob', 'Bob']`).
    * *Set:* Unordered, unique only (`{'Bob'}`).
* **Input Normalization:**
    * Used `.lower()` on the user's input to ensure the "stop" command works regardless of capitalization (e.g., "STOP" vs "stop").
* **Length Function (`len()`):**
    * Used `len()` to compare the size of the original list vs. the filtered set to see how many duplicates were removed.

## 💻 How to Run
1. Navigate to the project directory:
   ```bash
   cd 50-days-of-python/Day_09_Unique_Names
