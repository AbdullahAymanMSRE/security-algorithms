# Classical Encryption Application

A desktop application built with PyQt5 that implements three classical encryption algorithms: Caesar Cipher, Rail Fence Cipher, and Playfair Cipher. This application allows users to encrypt and decrypt messages using these historical cryptographic methods.

## Features

- **Three Classic Encryption Algorithms**:
  - Caesar Cipher - A substitution cipher where each letter is shifted by a fixed number of positions
  - Rail Fence Cipher - A transposition cipher that arranges text in a zigzag pattern across "rails"
  - Playfair Cipher - A digraph substitution cipher that uses a 5x5 grid of letters

- **User-Friendly Interface**:
  - Simple mode selection between encryption and decryption
  - Algorithm-specific key inputs
  - Real-time output display
  - Clean and intuitive layout

## Requirements

- Python 3.6+
- PyQt5

## Installation

1. Ensure you have Python installed on your system
2. Install the required dependencies:
   ```
   pip install PyQt5
   ```
3. Clone or download the repository
4. Run the application:
   ```
   python encryption_app.py
   ```

## Usage

1. **Select Mode**: Choose between "Encrypt" and "Decrypt"
2. **Select Algorithm**: Choose one of the three encryption algorithms
3. **Enter Key**:
   - For Caesar Cipher: Enter a numeric shift value
   - For Rail Fence Cipher: Enter the number of rails
   - For Playfair Cipher: Enter a keyword to generate the cipher matrix
4. **Enter Text**: Type or paste the text you want to process in the "Input Text" field
5. **Process**: Click the "Process" button to see the result in the "Output Text" field

## Algorithm Details

### Caesar Cipher
- Each letter in the plaintext is shifted a certain number of places down the alphabet
- Non-alphabetic characters remain unchanged
- The shift value wraps around the alphabet (modulo 26)

### Rail Fence Cipher
- The plaintext is written in a zigzag pattern across a number of rails
- The ciphertext is formed by reading off each rail sequentially
- Spaces are removed during encryption

### Playfair Cipher
- Uses a 5×5 grid of letters (I and J are combined)
- Text is encrypted in pairs of letters (digraphs)
- Special rules apply for digraphs that fall in the same row, column, or form a rectangle

## License

This project is open-source and available for educational and personal use.

## Contributors

Created as a demonstration of classical cryptography techniques.
