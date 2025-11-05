class PermutationCipher:
    def __init__(self, key):
        self.key = key  # e.g., [3, 1, 2]

    def encrypt(self, plaintext):
        plaintext = plaintext.replace(" ", "")  # remove spaces
        ciphertext = ""
        key_len = len(self.key)

        for i in range(0, len(plaintext), key_len):
            block = plaintext[i:i+key_len]
            if len(block) < key_len:
                block += " " * (key_len - len(block))  # pad with space
            for index in self.key:
                if index <= len(block):
                    ciphertext += block[index-1]  # 1-indexed key
        return ciphertext

