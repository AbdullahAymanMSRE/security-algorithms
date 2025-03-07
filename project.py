import string
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QComboBox, QGroupBox,
                             QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                             QPushButton, QRadioButton, QTextEdit, QVBoxLayout,
                             QWidget)


class EncryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Classical Encryption Application")
        self.setGeometry(100, 100, 800, 600)
        
        self.init_ui()
        
    def init_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Mode selection (encrypt/decrypt)
        mode_group = QGroupBox("Mode")
        mode_layout = QHBoxLayout()
        self.encrypt_radio = QRadioButton("Encrypt")
        self.decrypt_radio = QRadioButton("Decrypt")
        self.encrypt_radio.setChecked(True)  # Default to encrypt
        
        mode_layout.addWidget(self.encrypt_radio)
        mode_layout.addWidget(self.decrypt_radio)
        mode_group.setLayout(mode_layout)
        main_layout.addWidget(mode_group)
        
        # Algorithm selection
        algo_group = QGroupBox("Algorithm")
        algo_layout = QHBoxLayout()
        self.algo_combo = QComboBox()
        self.algo_combo.addItems(["Caesar Cipher", "Rail Fence Cipher", "Playfair Cipher"])
        self.algo_combo.currentIndexChanged.connect(self.update_key_section)
        algo_layout.addWidget(self.algo_combo)
        algo_group.setLayout(algo_layout)
        main_layout.addWidget(algo_group)
        
        # Key input section
        self.key_section = QGroupBox("Encryption Key")
        self.key_layout = QVBoxLayout()
        
        # Caesar cipher widgets
        self.caesar_widget = QWidget()
        caesar_layout = QHBoxLayout()
        caesar_layout.addWidget(QLabel("Shift Value:"))
        self.shift_input = QLineEdit()
        self.shift_input.setPlaceholderText("Enter a number (e.g., 3)")
        caesar_layout.addWidget(self.shift_input)
        self.caesar_widget.setLayout(caesar_layout)
        
        # Rail Fence widgets
        self.rail_fence_widget = QWidget()
        rail_fence_layout = QHBoxLayout()
        rail_fence_layout.addWidget(QLabel("Number of Rails:"))
        self.rails_input = QLineEdit()
        self.rails_input.setPlaceholderText("Enter number of rails (e.g., 3)")
        rail_fence_layout.addWidget(self.rails_input)
        self.rail_fence_widget.setLayout(rail_fence_layout)
        
        # Playfair widgets
        self.playfair_widget = QWidget()
        playfair_layout = QHBoxLayout()
        playfair_layout.addWidget(QLabel("Playfair Key:"))
        self.playfair_input = QLineEdit()
        self.playfair_input.setPlaceholderText("Enter key word (e.g., MONARCHY)")
        playfair_layout.addWidget(self.playfair_input)
        self.playfair_widget.setLayout(playfair_layout)
        
        # Add all widgets to the key layout
        self.key_layout.addWidget(self.caesar_widget)
        self.key_layout.addWidget(self.rail_fence_widget)
        self.key_layout.addWidget(self.playfair_widget)
        
        # Initially hide the ones we don't need
        self.rail_fence_widget.hide()
        self.playfair_widget.hide()
        
        self.key_section.setLayout(self.key_layout)
        main_layout.addWidget(self.key_section)
        
        # Input and output text fields
        text_layout = QHBoxLayout()
        
        input_group = QGroupBox("Input Text")
        input_layout = QVBoxLayout()
        self.input_text = QTextEdit()
        input_layout.addWidget(self.input_text)
        input_group.setLayout(input_layout)
        
        output_group = QGroupBox("Output Text")
        output_layout = QVBoxLayout()
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        output_layout.addWidget(self.output_text)
        output_group.setLayout(output_layout)
        
        text_layout.addWidget(input_group)
        text_layout.addWidget(output_group)
        main_layout.addLayout(text_layout)
        
        # Process button
        process_layout = QHBoxLayout()
        self.process_btn = QPushButton("Process")
        self.process_btn.clicked.connect(self.process_text)
        process_layout.addStretch()
        process_layout.addWidget(self.process_btn)
        main_layout.addLayout(process_layout)
        
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    
    def update_key_section(self, index):
        # Hide all key input widgets first
        self.caesar_widget.hide()
        self.rail_fence_widget.hide()
        self.playfair_widget.hide()
        
        # Show the relevant widget based on selected algorithm
        if index == 0:  # Caesar
            self.caesar_widget.show()
            self.key_section.setTitle("Caesar Cipher Key")
        elif index == 1:  # Rail Fence
            self.rail_fence_widget.show()
            self.key_section.setTitle("Rail Fence Key")
        else:  # Playfair
            self.playfair_widget.show()
            self.key_section.setTitle("Playfair Cipher Key")
    
    def process_text(self):
        input_text = self.input_text.toPlainText()
        if not input_text.strip():
            self.output_text.setText("Please enter some text to process.")
            return
        
        # Get encryption/decryption mode
        encrypt_mode = self.encrypt_radio.isChecked()
        
        # Process based on selected algorithm
        algo_index = self.algo_combo.currentIndex()
        
        try:
            if algo_index == 0:  # Caesar
                shift = self.shift_input.text().strip()
                if not shift or not shift.isdigit():
                    self.output_text.setText("Please enter a valid shift value (integer).")
                    return
                shift = int(shift) % 26
                
                if encrypt_mode:
                    result = self.caesar_encrypt(input_text, shift)
                else:
                    result = self.caesar_decrypt(input_text, shift)
                    
            elif algo_index == 1:  # Rail Fence
                rails = self.rails_input.text().strip()
                if not rails or not rails.isdigit():
                    self.output_text.setText("Please enter a valid number of rails (integer).")
                    return
                rails = int(rails)
                
                if rails < 2:
                    self.output_text.setText("Number of rails must be at least 2.")
                    return
                    
                if encrypt_mode:
                    result = self.rail_fence_encrypt(input_text, rails)
                else:
                    result = self.rail_fence_decrypt(input_text, rails)
                    
            else:  # Playfair
                key = self.playfair_input.text().strip().upper()
                if not key:
                    self.output_text.setText("Please enter a valid key for Playfair cipher.")
                    return
                
                if encrypt_mode:
                    result = self.playfair_encrypt(input_text, key)
                else:
                    result = self.playfair_decrypt(input_text, key)
            
            self.output_text.setText(result)
            
        except Exception as e:
            self.output_text.setText(f"Error: {str(e)}")
    
    # Caesar Cipher Implementation
    def caesar_encrypt(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        return result
    
    def caesar_decrypt(self, text, shift):
        return self.caesar_encrypt(text, 26 - shift)
    
    # Rail Fence Cipher Implementation
    def rail_fence_encrypt(self, text, rails):
        if rails <= 1:
            return text
            
        # Remove spaces for traditional rail fence implementation
        text = ''.join(text.split())
        
        # Initialize the rail matrix
        fence = [[''] * len(text) for _ in range(rails)]
        
        # Fill the rail matrix
        rail, direction = 0, 1
        for i in range(len(text)):
            fence[rail][i] = text[i]
            rail += direction
            
            # Change direction when we reach the top or bottom rail
            if rail == rails - 1 or rail == 0:
                direction = -direction
        
        # Read off the rail fence
        result = ''
        for i in range(rails):
            for j in range(len(text)):
                if fence[i][j] != '':
                    result += fence[i][j]
                    
        return result
    
    def rail_fence_decrypt(self, text, rails):
        if rails <= 1:
            return text
            
        # Remove spaces
        text = ''.join(text.split())
        
        # Initialize the rail matrix
        fence = [[None] * len(text) for _ in range(rails)]
        
        # Mark the zig-zag pattern in the matrix
        rail, direction = 0, 1
        for i in range(len(text)):
            fence[rail][i] = '*'
            rail += direction
            
            if rail == rails - 1 or rail == 0:
                direction = -direction
        
        # Fill the matrix with the ciphertext
        index = 0
        for i in range(rails):
            for j in range(len(text)):
                if fence[i][j] == '*' and index < len(text):
                    fence[i][j] = text[index]
                    index += 1
        
        # Read off the rail fence in zig-zag order
        result = ''
        rail, direction = 0, 1
        for i in range(len(text)):
            result += fence[rail][i]
            rail += direction
            
            if rail == rails - 1 or rail == 0:
                direction = -direction
                
        return result

    # Playfair Cipher Implementation
    def create_playfair_matrix(self, key):
        # Create 5x5 matrix from the key
        key = key.upper().replace("J", "I")  # Replace J with I as per Playfair rules
        
        # Remove duplicates while preserving order
        key_chars = []
        for char in key:
            if char.isalpha() and char not in key_chars:
                key_chars.append(char)
        
        # Fill the matrix with the key and remaining alphabet
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: no J
        for char in alphabet:
            if char not in key_chars:
                key_chars.append(char)
        
        # Convert to 5x5 matrix
        matrix = []
        for i in range(0, 25, 5):
            matrix.append(key_chars[i:i+5])
            
        return matrix
    
    def find_position(self, matrix, char):
        char = char.upper()
        if char == 'J':
            char = 'I'
            
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char:
                    return i, j
        return -1, -1
    
    def playfair_encrypt(self, text, key):
        # Prepare the text: convert to uppercase, replace J with I, and group into digraphs
        text = text.upper().replace("J", "I")
        text = ''.join([c for c in text if c.isalpha()])  # Remove non-alphabetic characters
        
        # Add padding if necessary
        if len(text) % 2 != 0:
            text += 'X'
            
        # Group into digraphs and handle same letter in a digraph
        digraphs = []
        i = 0
        while i < len(text):
            if i + 1 < len(text):
                if text[i] == text[i+1]:
                    digraphs.append(text[i] + 'X')
                    i += 1
                else:
                    digraphs.append(text[i] + text[i+1])
                    i += 2
            else:
                digraphs.append(text[i] + 'X')
                i += 1
                
        # Create the Playfair matrix
        matrix = self.create_playfair_matrix(key)
        
        # Encrypt each digraph
        result = ""
        for digraph in digraphs:
            row1, col1 = self.find_position(matrix, digraph[0])
            row2, col2 = self.find_position(matrix, digraph[1])
            
            if row1 == row2:  # Same row
                result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Same column
                result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  # Rectangle case
                result += matrix[row1][col2] + matrix[row2][col1]
        
        return result
    
    def playfair_decrypt(self, text, key):
        # Prepare the ciphertext
        text = text.upper().replace("J", "I")
        text = ''.join([c for c in text if c.isalpha()])
        
        # Add padding if necessary
        if len(text) % 2 != 0:
            text += 'X'
            
        # Group into digraphs
        digraphs = [text[i:i+2] for i in range(0, len(text), 2)]
        
        # Create the Playfair matrix
        matrix = self.create_playfair_matrix(key)
        
        # Decrypt each digraph
        result = ""
        for digraph in digraphs:
            row1, col1 = self.find_position(matrix, digraph[0])
            row2, col2 = self.find_position(matrix, digraph[1])
            
            if row1 == row2:  # Same row
                result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Same column
                result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:  # Rectangle case
                result += matrix[row1][col2] + matrix[row2][col1]
        
        return result

def main():
    app = QApplication(sys.argv)
    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
