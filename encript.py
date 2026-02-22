import random
import string

# Characters to use
chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)

# Create shuffled key
key = chars.copy()
random.shuffle(key)

# --- Encryption ---
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    if letter in chars:
        index = chars.index(letter)
        cipher_text += key[index]
    else:
        cipher_text += letter

print(f"\nPlain Text: {plain_text}")
print(f"Cipher Text: {cipher_text}")

# --- Decryption ---
cipher_input = input("\nEnter a message to decrypt: ")
decrypted_text = ""

for letter in cipher_input:
    if letter in key:  
        index = key.index(letter)
        decrypted_text += chars[index]
    else:
        decrypted_text += letter

print(f"\nCipher Text: {cipher_input}")
print(f"Decrypted Text: {decrypted_text}")