# 🔐 Caesar Cipher Encryption & Decryption Tool

A beginner-friendly cybersecurity project that demonstrates the fundamental concepts of **encryption and decryption** using the **Caesar Cipher** algorithm.

This project was developed as part of **DecodeLabs Cybersecurity Project 2**, focusing on understanding basic cryptographic concepts and data confidentiality.

---

## 📌 Project Overview

The **Caesar Cipher Encryption & Decryption Tool** allows users to enter a message and apply a user-defined shift key to encrypt and decrypt text.

The program demonstrates how plaintext can be transformed into ciphertext through a simple mathematical shifting process and then converted back to the original plaintext through decryption.

### Example

```text
Original Message: HELLO
Shift Key: 3

Encrypted Text: KHOOR
Decrypted Text: HELLO
```

---

## 🎯 Objectives

The main objectives of this project are:

* Understand the basic concept of encryption.
* Understand the process of decryption.
* Implement a simple cryptographic algorithm.
* Apply a user-defined shift key.
* Demonstrate reversible data transformation.
* Understand the limitations of basic encryption techniques.

---

## 🔑 Key Features

* 🔒 Encrypt user-provided text.
* 🔓 Decrypt encrypted text.
* 🔑 Support for custom shift keys.
* 🔠 Handles uppercase and lowercase letters.
* 🔢 Preserves numbers and special characters.
* 🛡️ Includes basic input validation.
* 🔄 Demonstrates reversible encryption and decryption logic.
* 💻 Simple command-line interface.

---

## 🧠 How Caesar Cipher Works

The Caesar Cipher is a substitution cipher that shifts each letter in the alphabet by a fixed number of positions.

For example, with a shift key of `3`:

```text
A → D
B → E
C → F
D → G
```

Therefore:

```text
HELLO
```

becomes:

```text
KHOOR
```

### Encryption

```text
Encrypted Character = Original Character + Shift Key
```

### Decryption

```text
Original Character = Encrypted Character - Shift Key
```

The encryption and decryption process uses modulo `26` to ensure that the characters remain within the alphabet.

---

## 🛠️ Technologies Used

* **Python 3**
* **VS Code**
* **Git & GitHub**

No external Python libraries are required.

---

## 📂 Project Structure

```text
caesar-cipher-tool/
│
├── caesar_cipher.py
├── README.md
└── screenshots/
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Dinijaya633/Project-2-caesar-cipher-tool.git
```

### 2. Navigate to the Project Directory

```bash
cd caesar-cipher-tool
```

### 3. Check Python Installation

```bash
python --version
```

If `python` does not work, try:

```bash
py --version
```

### 4. Run the Program

```bash
python caesar_cipher.py
```

Or:

```bash
py caesar_cipher.py
```

---

## 🚀 How to Use

1. Run the Python program.
2. Enter the message you want to process.
3. Enter a shift key.
4. The program encrypts the message.
5. The encrypted message is displayed.
6. The program decrypts the encrypted message.
7. The original message is displayed again.

### Example Output

```text
===== Caesar Cipher Tool =====

Enter your message: Hello World
Enter shift key: 3

Encrypted text: Khoor Zruog
Decrypted text: Hello World
```

---

## 🧪 Testing

The program should be tested using different types of input.

### Test Case 1 – Basic Text

```text
Input: HELLO
Shift: 3

Expected Encrypted Output: KHOOR
Expected Decrypted Output: HELLO
```

### Test Case 2 – Mixed Case

```text
Input: Hello World
Shift: 5

Expected Encrypted Output: Mjqqt Btwqi
```

### Test Case 3 – Numbers and Symbols

```text
Input: Hello123!
Shift: 5
```

Numbers and special characters should remain unchanged.

### Test Case 4 – Full Alphabet Shift

```text
Shift: 26
```

The encrypted text should remain the same as the original text.

---

## ⚠️ Security Limitations

The Caesar Cipher is **not considered secure for real-world data protection**.

Its main limitations include:

* Only 26 possible shift values exist.
* It can easily be broken using brute-force attacks.
* Frequency analysis can reveal the original message.
* It does not provide modern cryptographic security.
* It should not be used to protect passwords or sensitive information.

This project is intended for **educational purposes** to demonstrate fundamental encryption and decryption concepts.

For real-world applications, modern cryptographic algorithms such as **AES** and secure encryption protocols should be used.

---

## 🔮 Future Improvements

Possible future improvements include:

* Add a graphical user interface (GUI).
* Add a Vigenère Cipher implementation.
* Support file encryption and decryption.
* Add encryption history.
* Add password-based encryption.
* Implement modern encryption algorithms for educational comparison.
* Add automated unit testing.
* Improve error handling and user experience.

---

## 🎓 Learning Outcomes

Through this project, I gained practical knowledge of:

* Basic cryptography concepts.
* Encryption and decryption.
* Caesar Cipher implementation.
* Character manipulation in Python.
* User input handling.
* Basic error handling.
* The importance of data confidentiality.
* The limitations of classical cryptographic algorithms.

---

## 👨‍💻 Author

**Dinijaya Peiris**

Cybersecurity Undergraduate
Sri Lanka Institute of Information Technology (SLIIT)

---

## 📜 Project Context

This project was completed as part of **DecodeLabs Cybersecurity Project 2: Basic Encryption & Decryption**.

The project focuses on developing a practical understanding of fundamental cryptographic techniques through hands-on implementation.

---

⭐ If you found this project useful, feel free to explore the repository and learn more about basic cryptography.
