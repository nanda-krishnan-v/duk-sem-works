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

plainText = format(0b1101001010110110, '016b')

"""converts the plainText to the correspoding
   binary , b means binary and 016 means 16 bit ,
   if they are not filled they will add zero till 16 bit"""

key = format(0b0110110110010100, '016b')  #same as the plainText

def apply_sBox(block, sBox):
    substituted = ""
    for i in range(0, 16, 4):
        index = int(block[i:i+4], 2)  # Convert 4-bit binary string to integer
        substituted += format(sBox[index], '04b')  # Convert back to 4-bit binary
    return substituted

def apply_XOR(block, key):
    result = ""
    for i in range(16):
        result += str(int(block[i]) ^ int(key[i]))  # XOR operation
    return result

def apply_pBox(block, pBox):
    permuted = ""  # Start with an empty string
    for i in pBox:  # Loop through each index in pBox
        permuted += block[i]  # Get the bit at position i and add it to permuted
    return permuted  # Return the rearranged binary string


# Apply transformations
xor_result = apply_XOR(plainText, key) # plaintext XOR Key
substituted_result = apply_sBox(xor_result, sBox) # applying s-box
ciphertext = apply_pBox(substituted_result, pBox) # applying permutations

print("ENCRYPTION")
print("Plaintext: ", plainText)
print("Ciphertext:", ciphertext)

pbox_reversed = apply_pBox(ciphertext, inverse_pBox)  # Reverse P-Box
sbox_reversed = apply_sBox(pbox_reversed, inverse_sBox)  # Reverse S-Box
decrypted_text = apply_XOR(sbox_reversed, key)  # Reverse XOR

print()

print("DECRYPTION")
print("Ciphertext:", ciphertext)
print("Plaintext:  ", decrypted_text)