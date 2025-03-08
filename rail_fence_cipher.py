class RailFenceCipher:
    def encrypt(self, text, rails):
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
    
    def decrypt(self, text, rails):
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
