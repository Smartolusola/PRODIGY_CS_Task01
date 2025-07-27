# caesar_cipher.py

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift_amount = shift if mode == 'encrypt' else -shift
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    text = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    mode = input("Choose mode (encrypt/decrypt): ").lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected.")
        return

    output = caesar_cipher(text, shift, mode)
    print(f"\nResult: {output}")

if __name__ == "__main__":
    main()
