import string

def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Args:
        text (str): The input message to be encrypted or decrypted.
        shift (int): The number of positions to shift each letter.
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
        str: The processed (encrypted or decrypted) text.
    """
    result = ""
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            start = ord('a')
            # Apply shift and wrap around the alphabet (26 letters)
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            start = ord('A')
            # Apply shift and wrap around the alphabet (26 letters)
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def main():
    """
    Main function to interact with the user for Caesar Cipher operations.
    """
    print("Welcome to the Caesar Cipher Tool!")

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (an integer): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the shift value.")
            encrypted_message = caesar_cipher(message, shift, 'encrypt')
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (an integer): "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer for the shift value.")
            decrypted_message = caesar_cipher(message, shift, 'decrypt')
            print(f"Decrypted message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the Caesar Cipher Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
