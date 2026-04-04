# ⚙️ Config File Updater (Python)

## 👨‍💻 About This Project

I am currently learning Python and building small practical scripts to strengthen my understanding of scripting and automation.

This project is a simple utility that allows users to update key-value pairs inside configuration files programmatically instead of editing them manually.

---

## 🧠 What I Learned

* File handling in Python (`open`, `readlines`, `write`)
* Working with strings and formatting
* Using functions for modular code
* Handling user input dynamically
* Basic automation concepts

---

## ⚙️ How It Works

1. User provides:

   * File path
   * Key to update
   * New value

2. Script:

   * Reads the file content
   * Searches for the given key
   * Updates the corresponding value
   * Writes the updated content back to the file

---

## 🧪 Example

### Input:

```
file path enter kar bhai: test.conf
key where change is required: port
what should be the updated value: 8080
```

### Before:

```
port = 3000
host = localhost
```

### After:

```
port = 8080
host = localhost
```

---

## 🛠️ Tech Used

* Python
* Built-in file handling functions

---

## 📂 Project Structure

```
config-file-updater/
 ├── program.py
 ├── test.conf
 └── README.md
```

---

## 🚀 Future Improvements

* Add backup before modifying files
* Convert script into CLI tool using `argparse`
* Support different file formats (JSON, YAML)
* Add validation for file path
* Improve key matching logic

---

## 💡 Why I Built This

As a beginner, I wanted to move beyond theory and build something practical that solves a real problem.
This project helped me understand how automation can reduce manual work in configuration management.

---

## ⚠️ Limitations

* Matches keys using simple string search (may match partial keys)
* Works best with simple `key = value` formatted files

---

## 🎯 Goal

To keep building small projects like this and gradually improve my Python and automation skills.
