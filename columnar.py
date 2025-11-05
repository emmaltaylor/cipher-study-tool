# this is the columnar cipher, that takes one string/word and then another as the key; and then
# it encrypts the first string using the columnar cipher method.

class ColumnarCipher:
    def __init__(self, key):
        self.key = key.upper()  

    def encrypt(self, plaintext):
        plaintext = plaintext.replace(" ", "").upper()
        num_cols = len(self.key)
        num_rows = -(-len(plaintext) // num_cols)  # ceiling division

        # Fill the matrix row by row
        matrix = [["" for _ in range(num_cols)] for _ in range(num_rows)]
        index = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if index < len(plaintext):
                    matrix[r][c] = plaintext[index]
                    index += 1

        # Read columns in order determined by sorted key letters
        sorted_indices = sorted(range(len(self.key)), key=lambda x: self.key[x])
        ciphertext = ""
        for c in sorted_indices:
            for r in range(num_rows):
                if matrix[r][c]:
                    ciphertext += matrix[r][c]
        return ciphertext
