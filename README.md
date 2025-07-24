Caesar Cipher Encryptor/Decryptor

Overview

This Python program implements the classic Caesar Cipher algorithm, allowing users to encrypt and decrypt text messages using a specified shift value. It's a simple yet fundamental cryptographic tool, perfect for understanding basic encryption concepts.

Features

1. Encryption: Scramble your messages to keep them secret.
2. Decryption: Unscramble encrypted messages back to their original form.
3. User-Friendly Interface: Simple command-line prompts for easy interaction.
4. Case Preservation: Handles both uppercase and lowercase letters.
5. Non-Alphabetic Character Preservation: Spaces, numbers, and punctuation remain unchanged.

How the Caesar Cipher Works
The Caesar Cipher is one of the oldest and simplest methods of encryption. It's a type of substitution cipher where each letter in the plaintext (original message) is replaced by a letter some fixed number of positions down or up the alphabet. For example, with a left shift of 3, 'D' would be replaced by 'A', 'E' would become 'B', and so on.

Getting Started

Prerequisites
You only need Python installed on your system. This program was developed with Python 3.x.
1. Installation
Clone the repository (or download the file):
If you're using Git, you can clone this repository to your local machine:git clone https://github.com/obaprosper/PRODIGY_CS_01.git

2. Navigate to the program directory:
Ensure you are in the directory where 'Caesar Cipher Encryptor and Decryptor.py' is located.

Usage
To run the program, open your terminal or command prompt, navigate to the directory where you saved the caesar_cipher.py file, and execute the following command:
python 'Caesar Cipher Encryptor and Decryptor.py'

The program will then present you with a menu:Welcome to the Caesar Cipher Tool!

Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter your choice (1, 2, or 3):

Options:
1. Encrypt a message:
   Enter your message.
   Enter a positive integer for the shift value (e.g., 3 to shift 'A' to 'D').
2. Decrypt a message:
   Enter the encrypted message.
   Enter the same shift value that was used for encryption. The program will automatically reverse the shift.
3. Exit:
   Quits the program.

   ExampleLet's say you want to encrypt "HELLO WORLD" with a shift of 3:Enter your choice (1, 2, or 3): 1
Enter the message to encrypt: HELLO WORLD
Enter the shift value (an integer): 3
Encrypted message: KHOOR ZRUOG
To decrypt "KHOOR ZRUOG" with a shift of 3:Enter your choice (1, 2, or 3): 2
Enter the message to decrypt: KHOOR ZRUOG
Enter the shift value (an integer): 3
Decrypted message: HELLO WORLD
ContributingFeel free to fork this repository, make improvements, and submit pull requests. Suggestions for new features or bug fixes are always welcome!LicenseThis project is open source and available under the MIT License.
