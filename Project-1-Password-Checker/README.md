# 🔐 Password Strength Checker

## DecodeLabs Internship – Cyber Security Project 1

A simple cybersecurity project that evaluates the strength of a password based on basic security requirements.

## 📌 Project Overview

The Password Strength Checker is designed to check whether a password is **Weak, Medium, or Strong**.

The application evaluates a password based on:

* Password length
* Uppercase letters
* Numbers
* Special symbols

The project demonstrates basic cybersecurity concepts, string handling, input validation, and conditional logic.

## 🎯 Project Goal

The goal of this project is to create a program that can evaluate password strength and provide users with useful feedback about improving password security.

## ✨ Features

* 🔐 Password strength evaluation
* 📏 Password length validation
* 🔠 Uppercase letter detection
* 🔢 Number detection
* 🔣 Special symbol detection
* 📊 Weak, Medium, or Strong classification
* 💡 Security recommendations
* 👁️ Show/Hide password option
* 📱 Responsive web interface

## 🛠️ Technologies Used

### Web Version

* HTML5
* CSS3
* JavaScript

### Python Version

* Python 3
* String handling
* Conditional logic

## 📂 Project Structure

```text
Project-1-Password-Checker
│
├── index.html
├── style.css
├── script.js
├── password_checker.py
└── README.md
```

## 🔍 Password Strength Criteria

The application checks four main requirements:

| Requirement | Description                                   |
| ----------- | --------------------------------------------- |
| Length      | Password should contain at least 8 characters |
| Uppercase   | Password should contain an uppercase letter   |
| Number      | Password should contain at least one number   |
| Symbol      | Password should contain a special symbol      |

## 📊 Strength Classification

The password is evaluated based on the number of requirements it satisfies.

* **Weak** – 0 to 1 requirements satisfied
* **Medium** – 2 to 3 requirements satisfied
* **Strong** – All 4 requirements satisfied

### Example

```text
hello
```

Result:

```text
Weak
```

```text
Hello123
```

Result:

```text
Medium
```

```text
Hello@123
```

Result:

```text
Strong
```

## 🚀 How to Run the Web Version

### Step 1: Open the project

Open the project folder in Visual Studio Code.

### Step 2: Check the files

Make sure the following files are available:

```text
index.html
style.css
script.js
```

### Step 3: Run the application

Open `index.html` in a web browser.

Alternatively, install the **Live Server** extension in Visual Studio Code and select:

```text
Right Click → Open with Live Server
```

## 🐍 How to Run the Python Version

Make sure Python is installed on your computer.

Open the terminal inside the project folder and run:

```bash
python password_checker.py
```

If your system uses `python3`, run:

```bash
python3 password_checker.py
```

## 🔒 Security Note

This project is intended for educational purposes and demonstrates basic password-strength evaluation.

The web version performs password checks locally in the browser and does not require a backend server.

For real-world applications, passwords should never be stored or transmitted as plaintext.

## 📚 Learning Outcomes

Through this project, I developed an understanding of:

* Basic password security principles
* String handling
* Conditional logic
* Input validation
* JavaScript event handling
* HTML and CSS web development
* Basic cybersecurity practices

## 🔮 Future Improvements

Possible future improvements include:

* Checking passwords against common or leaked password lists
* Adding a password entropy calculation
* Implementing a more advanced password scoring system
* Adding a password generator
* Improving accessibility
* Adding automated security tests

## 👨‍💻 Author

**Dinijaya Peiris**

Cyber Security Undergraduate

## 🛡️ Project

**DecodeLabs Cyber Security Internship – Project 1**

**Password Strength Checker**
