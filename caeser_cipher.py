class CaesarCipher:
    def encrypt(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        return result
    
    def decrypt(self, text, shift):
        return self.encrypt(text, 26 - shift)