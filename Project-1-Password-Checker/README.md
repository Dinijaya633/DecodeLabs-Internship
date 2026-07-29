# Password Strength Checker

A simple Python command-line tool that evaluates the strength of a password based on common security criteria and gives feedback on how to improve it.

## Features

- Checks password against key strength criteria:
  - Minimum length (8+ characters)
  - Presence of uppercase letters
  - Presence of lowercase letters
  - Presence of numbers
  - Presence of special symbols
- Assigns a strength rating: **Weak**, **Medium**, or **Strong**
- Provides specific recommendations to improve weak or medium passwords

## How It Works

The script scores a password based on how many of the following criteria it meets:

| Criteria | Description |
|---|---|
| Length | At least 8 characters |
| Uppercase | Contains at least one uppercase letter (A-Z) |
| Lowercase | Contains at least one lowercase letter (a-z) |
| Number | Contains at least one digit (0-9) |
| Symbol | Contains at least one special character (e.g. `!@#$%`) |

Based on the total score, the password is rated Weak, Medium, or Strong, and the tool prints suggestions for any missing criteria.

## Usage

Run the script from the command line:

```bash
python password_checker.py
```

You'll be prompted to enter a password, and the tool will display a full breakdown of its strength along with recommendations.

### Example Output

```
===================================
     PASSWORD STRENGTH CHECKER
===================================
Enter your password: Hello123

--- Password Strength Analysis ---
Password Length: 8 characters
Minimum Length (8+): Yes
Uppercase Letter: Yes
Number: Yes
Symbol: No

Password Strength: Medium

Recommendations:
- Add at least one special symbol.
```

## Requirements

- Python 3.x
- No external dependencies (uses only the built-in `string` module)

## Project Info

This project was built as part of the DecodeLabs Internship program.

## Author

Dinijaya