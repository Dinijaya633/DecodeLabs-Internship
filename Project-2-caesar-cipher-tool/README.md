# 🔐 Caesar Cipher Encryption & Decryption Tool

A beginner-friendly cybersecurity project that demonstrates the fundamental concepts of **encryption and decryption** using the **Caesar Cipher** algorithm.

This project was developed as part of **DecodeLabs Cybersecurity Project 2: Basic Encryption & Decryption**, with a focus on understanding basic cryptographic concepts, reversible encryption logic, and data confidentiality.

The project includes both a **Python command-line implementation** and a **simple interactive web-based interface**.

---

## 📌 Project Overview

The **Caesar Cipher Encryption & Decryption Tool** allows users to enter a message and apply a user-defined shift key to encrypt or decrypt text.

The project demonstrates how readable information (**plaintext**) can be transformed into encrypted information (**ciphertext**) using a basic mathematical shifting technique and then converted back into the original plaintext through the decryption process.

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
* Understand the basic concept of data confidentiality.
* Understand the limitations of classical encryption techniques.
* Implement the encryption and decryption process using Python.
* Create an interactive web interface for the cipher tool.

---

## 🔑 Key Features

### Python Command-Line Application

* 🔒 Encrypt user-provided text.
* 🔓 Decrypt encrypted text.
* 🔑 Support for custom shift keys.
* 🔠 Handles uppercase and lowercase letters.
* 🔢 Preserves numbers and special characters.
* 💻 Simple command-line interface.
* 🔄 Demonstrates reversible encryption and decryption logic.

### Interactive Web Application

* 🌐 Browser-based Caesar Cipher tool.
* 🔒 Encrypt text directly from the web interface.
* 🔓 Decrypt text directly from the web interface.
* 🔑 Select a custom shift key from 0 to 25.
* ➕ Increase or decrease the shift key using buttons.
* 📝 Display character count.
* 📋 Copy encrypted or decrypted results.
* 🗑️ Clear the input and output fields.
* 📱 Responsive design for different screen sizes.
* 🚫 No external libraries or frameworks required.

---

## 🧠 How Caesar Cipher Works

The Caesar Cipher is a basic substitution cipher that shifts each letter in the alphabet by a fixed number of positions.

For example, with a shift key of `3`:

```text
A → D
B → E
C → F
D → G
```

The complete alphabet transformation is:

```text
Original:

A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Shift +3:

D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

Therefore:

```text
HELLO
```

becomes:

```text
KHOOR
```

---

## 🔒 Encryption Process

During encryption, each letter is shifted forward according to the selected shift key.

```text
Plaintext
    ↓
Apply Shift Key
    ↓
Caesar Cipher Algorithm
    ↓
Ciphertext
```

### Example

```text
Plaintext: HELLO
Shift Key: 3

H → K
E → H
L → O
L → O
O → R

Ciphertext: KHOOR
```

The encryption logic can be represented as:

```text
Encrypted Character = Original Character + Shift Key
```

The algorithm uses modulo `26` to ensure that the letters wrap around when reaching the end of the alphabet.

---

## 🔓 Decryption Process

Decryption reverses the encryption process by shifting each letter backward using the same shift key.

```text
Ciphertext
    ↓
Apply Reverse Shift
    ↓
Caesar Cipher Algorithm
    ↓
Plaintext
```

### Example

```text
Ciphertext: KHOOR
Shift Key: 3

K → H
H → E
O → L
O → L
R → O

Plaintext: HELLO
```

The decryption logic can be represented as:

```text
Original Character = Encrypted Character - Shift Key
```

---

## 🛠️ Technologies Used

### Python Application

* **Python 3**
* **VS Code**

### Web Application

* **HTML5**
* **CSS3**
* **JavaScript**

### Development Tools

* **Visual Studio Code**
* **Git**
* **GitHub**

No external Python packages or JavaScript libraries are required.

---

## 📂 Project Structure

```text
Project-2-caesar-cipher-tool/
│
├── caesar_cipher.py
│
├── README.md
│
└── web/
    │
    ├── index.html
    ├── style.css
    └── script.js
```

### File Descriptions

| File               | Description                                             |
| ------------------ | ------------------------------------------------------- |
| `caesar_cipher.py` | Python command-line implementation of the Caesar Cipher |
| `README.md`        | Project documentation                                   |
| `web/index.html`   | Structure of the interactive web application            |
| `web/style.css`    | Styling and responsive design                           |
| `web/script.js`    | JavaScript encryption and decryption logic              |

---

# 🐍 Python Command-Line Application

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Dinijaya633/Project-2-caesar-cipher-tool.git
```

### 2. Navigate to the Project Directory

```bash
cd Project-2-caesar-cipher-tool
```

### 3. Check Python Installation

Run:

```bash
python --version
```

If `python` does not work, try:

```bash
py --version
```

You should have Python 3 installed.

### 4. Run the Program

Using Python:

```bash
python caesar_cipher.py
```

Or using the Python launcher:

```bash
py caesar_cipher.py
```

---

## 🚀 Using the Python Application

1. Run the Python program.
2. Enter the message you want to encrypt.
3. Enter a shift key.
4. The program encrypts the message.
5. The encrypted message is displayed.
6. The program decrypts the encrypted message.
7. The decrypted message is displayed.

### Example

```text
Enter your message: Hello World
Enter shift key: 3

Encrypted text: Khoor Zruog
Decrypted text: Hello World
```

---

# 🌐 Interactive Web Application

The project also includes a simple browser-based interface for performing Caesar Cipher encryption and decryption.

The web application provides an easy-to-use interface where users can:

* Enter plaintext or ciphertext.
* Select a shift key.
* Encrypt text.
* Decrypt text.
* Copy the result.
* Clear the tool and start again.

The web application performs the Caesar Cipher operations directly in the browser using JavaScript.

---

## 📂 Web Application Structure

```text
web/
│
├── index.html
├── style.css
└── script.js
```

### `index.html`

Contains the structure of the Caesar Cipher interface, including:

* Text input area.
* Shift key input.
* Encrypt button.
* Decrypt button.
* Result display.
* Copy button.
* Clear button.

### `style.css`

Provides the visual design of the web application, including:

* Dark cybersecurity-inspired interface.
* Responsive layout.
* Buttons and input styling.
* Mobile-friendly design.

### `script.js`

Contains the Caesar Cipher logic and interactive functionality, including:

* Encryption.
* Decryption.
* Shift key handling.
* Character counting.
* Copy-to-clipboard functionality.
* Clear functionality.

---

## ▶️ Running the Web Application

### Method 1 — Open Directly

Navigate to:

```text
Project-2-caesar-cipher-tool/web/
```

Open:

```text
index.html
```

The application will open in your default web browser.

---

### Method 2 — Using VS Code Live Server

For a better development experience, you can use the **Live Server** extension in Visual Studio Code.

1. Open the project in VS Code.
2. Open the `web` folder.
3. Open `index.html`.
4. Right-click the file.
5. Select **Open with Live Server**.

The Caesar Cipher web application will open in your browser.

---

## 🧪 Testing

The project should be tested using different types of input.

### Test Case 1 – Basic Text

```text
Input: HELLO
Shift: 3

Expected Encrypted Output: KHOOR
Expected Decrypted Output: HELLO
```

---

### Test Case 2 – Mixed Case

```text
Input: Hello World
Shift: 5

Expected Encrypted Output: Mjqqt Btwqi
```

The application should maintain the original uppercase and lowercase format.

---

### Test Case 3 – Numbers and Symbols

```text
Input: Hello123!
Shift: 5
```

Expected behavior:

```text
Mjqqt123!
```

Numbers and special characters should remain unchanged.

---

### Test Case 4 – Shift of 26

```text
Input: HELLO
Shift: 26
```

Expected behavior:

```text
HELLO
```

A shift of 26 results in the same text because the alphabet contains 26 letters.

---

### Test Case 5 – Empty Input

If the user attempts to encrypt or decrypt without entering any text, the application should display a message asking the user to enter text.

---

## 🔐 Security Limitations

The Caesar Cipher is **not considered secure for real-world data protection**.

Its main limitations include:

* Only 26 possible shift values exist.
* It can easily be broken using brute-force attacks.
* Frequency analysis can reveal patterns in the ciphertext.
* It does not provide modern cryptographic security.
* It should not be used to protect passwords or sensitive information.

The purpose of this project is to provide an educational understanding of the fundamental concepts behind encryption and decryption.

For real-world applications, modern cryptographic algorithms and secure encryption protocols should be used instead.

---

## 🎓 Learning Outcomes

Through this project, I gained practical knowledge of:

* Basic cryptography concepts.
* Encryption and decryption.
* Caesar Cipher implementation.
* Character manipulation in Python.
* JavaScript-based encryption and decryption.
* HTML and CSS for creating a web interface.
* User input handling.
* Shift-key based transformations.
* Reversible encryption logic.
* Basic data confidentiality concepts.
* The limitations of classical cryptographic algorithms.
* Developing a simple cybersecurity-focused web application.

---

## 🔮 Future Improvements

Possible future improvements include:

* Add a Vigenère Cipher implementation.
* Add additional classical cipher algorithms.
* Add automated unit testing.
* Improve error handling.
* Add file-based encryption and decryption for educational purposes.
* Improve the user interface.
* Add additional cryptography learning features.
* Compare classical ciphers with modern cryptographic algorithms.

---

## 👨‍💻 Author

**Dinijaya Peiris**

Cybersecurity Undergraduate
Sri Lanka Institute of Information Technology (SLIIT)

GitHub:
https://github.com/Dinijaya633

---

## 📜 Project Context

This project was completed as part of:

**DecodeLabs Cybersecurity Project 2: Basic Encryption & Decryption**

The project focuses on implementing a simple encryption and decryption technique using basic cryptographic logic. The project demonstrates encryption of user-provided text, decryption of encrypted text, and displaying the resulting outputs.

The project was extended with a simple interactive web-based interface to provide a more accessible way to experiment with the Caesar Cipher.

---

## ⚠️ Disclaimer

This project is intended for **educational purposes only**.

The Caesar Cipher is a classical cryptographic technique and should not be used to protect real-world sensitive or confidential information.

---

⭐ If you found this project useful, feel free to explore the repository and learn more about basic cryptography, encryption, and decryption.
