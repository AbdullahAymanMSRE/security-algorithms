class PlayfairCipher:
    def create_matrix(self, key):
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
    
    def encrypt(self, text, key):
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
        matrix = self.create_matrix(key)
        
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
    
    def decrypt(self, text, key):
        # Prepare the ciphertext
        text = text.upper().replace("J", "I")
        text = ''.join([c for c in text if c.isalpha()])
        
        # Add padding if necessary
        if len(text) % 2 != 0:
            text += 'X'
            
        # Group into digraphs
        digraphs = [text[i:i+2] for i in range(0, len(text), 2)]
        
        # Create the Playfair matrix
        matrix = self.create_matrix(key)
        
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