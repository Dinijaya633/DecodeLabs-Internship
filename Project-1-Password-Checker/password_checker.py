import string


def check_password_strength(password):
    # Check password length
    has_minimum_length = len(password) >= 8

    # Check for uppercase letters
    has_uppercase = any(char.isupper() for char in password)

    # Check for lowercase letters
    has_lowercase = any(char.islower() for char in password)

    # Check for numbers
    has_number = any(char.isdigit() for char in password)

    # Check for special symbols
    has_symbol = any(char in string.punctuation for char in password)

    # Calculate score
    score = 0

    if has_minimum_length:
        score += 1

    if has_uppercase:
        score += 1

    if has_number:
        score += 1

    if has_symbol:
        score += 1

    # Determine password strength
    if score <= 1:
        strength = "Weak"
    elif score <= 3:
        strength = "Medium"
    else:
        strength = "Strong"

    #results
    print("\n--- Password Strength Analysis ---")
    print(f"Password Length: {len(password)} characters")
    print(f"Minimum Length (8+): {'Yes' if has_minimum_length else 'No'}")
    print(f"Uppercase Letter: {'Yes' if has_uppercase else 'No'}")
    print(f"Number: {'Yes' if has_number else 'No'}")
    print(f"Symbol: {'Yes' if has_symbol else 'No'}")
    print(f"\nPassword Strength: {strength}")

    #recommendations
    if strength != "Strong":
        print("\nRecommendations:")

        if not has_minimum_length:
            print("- Use at least 8 characters.")

        if not has_uppercase:
            print("- Add at least one uppercase letter.")

        if not has_number:
            print("- Add at least one number.")

        if not has_symbol:
            print("- Add at least one special symbol.")

    return strength

print("===================================")
print("     PASSWORD STRENGTH CHECKER")
print("===================================")

password = input("Enter your password: ")

check_password_strength(password)