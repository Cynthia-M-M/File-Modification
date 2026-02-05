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

---

## 🏃‍♂️ How to Run

### 1. Clone the Repository
```bash
git clone [https://github.com/Cynthia-M-M/File-Modification.git](https://github.com/Cynthia-M-M/File-Modification.git)

```

### 2. Navigate to the Directory

```bash
cd File-Modification

```

### 3. Run the Script

```bash
python filereading.py

```

---

## 💻 Usage Scenarios

Here is how the program handles different situations:

### ✅ Scenario 1: Successful Modification

The user enters a valid filename, and the program processes it.

```text
Enter the filename to read: Books.txt
File read successfully!
Modified content written to 'Modified_Books.txt'.

```

### ❌ Scenario 2: File Not Found

The user enters a filename that does not exist. The program catches the error gracefully.

```text
Enter the filename to read: missing_file.txt
Error: The file 'missing_file.txt' does not exist. Please check the name and try again.

```

---

## 🧠 Code Logic (Preview)

Here is a snippet showing how the **Error Handling** is implemented:

```python
try:
    # Attempt to open and read the file
    with open(filename, "r") as file:
        content = file.read()
        
    # Modify content (e.g., converting to Uppercase)
    modified_content = content.upper()

    # Write to a new file
    with open("Modified_Books.txt", "w") as new_file:
        new_file.write(modified_content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError:
    print("Error: The file could not be read due to permission issues.")

```

---

## 📄 License

This project is open-source and created for educational purposes.

```

```
