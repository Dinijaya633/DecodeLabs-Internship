def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

message = input("Enter your message: ")
shift = int(input("Enter shift key: "))
encrypted = caesar_cipher(message, shift)
print("Encrypted text:", encrypted)
decrypted = caesar_cipher(encrypted, -shift)
print("Decrypted text:", decrypted)
