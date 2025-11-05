#this program prompts the user for what kind of cipher they would like to use to encryppt
# their word or phrase.

from permutation import PermutationCipher
from columnar import ColumnarCipher
from railfence import RailFenceCipher

def main():
    print("Welcome to the Cipher Program! Please select a cipher method:")
    print("1. Permutation Cipher")
    print("2. Columnar Cipher")
    print("3. Rail Fence Cipher")

    choice = input("Enter your choice (1-3): ")

    plaintext = input("Enter the plaintext: ")

    if choice == "1":
        key = [int(x) for x in input("Enter permutation key (e.g., 3 1 2): ").split()]
        cipher = PermutationCipher(key)
    elif choice == "2":
        key = input("Enter columnar key: ")
        cipher = ColumnarCipher(key)
    elif choice == "3":
        rails = int(input("Enter number of rails: "))
        cipher = RailFenceCipher(rails)
    else:
        print("Invalid choice.")
        return

    ciphertext = cipher.encrypt(plaintext)
    print(f"\nEncrypted Text: {ciphertext}")

if __name__ == "__main__":
    main()