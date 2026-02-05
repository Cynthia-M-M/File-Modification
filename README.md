# 📂 File Modification & Error Handling

![Python Banner](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📋 Project Overview

This project is a Python utility designed to demonstrate robust **File I/O operations**. The script securely reads a source file, programmatically modifies its content, and writes the result to a new destination file.

Crucially, it implements comprehensive **Exception Handling** to manage real-world edge cases, such as missing files, empty directories, or permission restrictions, ensuring the program does not crash unexpectedly.

---

## 🚀 Key Features

* **File Reading & Writing:** Opens external files for processing and saves changes to a new output file.
* **Content Modification:** Processes text data from the source before saving.
* **Robust Error Handling:**
  * Detects if a file does not exist (`FileNotFoundError`).
  * Handles empty files or unreadable formats.
  * manages permission errors.
* **Interactive CLI:** Prompts the user for input filenames dynamically.

---

## 🔧 Technologies Used

* **Python 3.x** - Core language for file manipulation and exception logic.

---

## 📂 Project Structure

```text
File-Modification/
│
├── filereading.py        # Main script for file operations
├── Books.txt             # Sample input file (Source)
├── Modified_Books.txt    # Generated output file (Destination)
├── example_files/        # Directory containing additional resources
└── README.md             # Project documentation
