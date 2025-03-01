#defining the s-box and p-box

sBox = {
    0: 14, 1: 4, 2: 13, 3: 1,
    4: 2, 5: 15, 6: 11, 7: 8,
    8: 3, 9: 10, 10: 6, 11: 12,
    12: 5, 13: 9, 14: 0, 15: 7
}
inverse_sBox = {
    14: 0, 4: 1, 13: 2, 1: 3,
    2: 4, 15: 5, 11: 6, 8: 7,
    3: 8, 10: 9, 6: 10, 12: 11,
    5: 12, 9: 13, 0: 14, 7: 15
}

pBox = [15, 0, 8, 7, 12, 3, 9, 5, 6, 1, 10, 4, 2, 14, 13, 11]
inverse_pBox = [1, 9, 12, 5, 11, 7, 8, 3, 2, 6, 10, 15, 4, 14, 13, 0]

def ecb_encrypt(plaintext, key):
    ciphertext = ""
    for c in plaintext:
        ciphertext += chr(ord(c) + key)  # Shift each character
    return ciphertext

def ecb_decrypt(ciphertext, key):
    decrypted_text = ""
    for c in ciphertext:
        decrypted_text += chr(ord(c) - key)  # Reverse shift
    return decrypted_text.rstrip()  # Remove padding spaces

plaintext = input("Enter a plaintext message: ")

# Pad the input to be a multiple of 16
while len(plaintext) % 16 != 0:
    plaintext += " "  # Adding spaces as padding

key = 1  # Simple shift key

ciphertext = ecb_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = ecb_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
