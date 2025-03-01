
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

def get_valid_16bit_input(prompt):
    value = input(prompt)
    while len(value) != 16:
        valid = True  # Assume input is valid
        for c in value:
            if c != '0' and c != '1':  # Check if input contains only 0s and 1s
                valid = False
                break  # Stop checking further

        if not valid:
            value = input("Invalid input! " + prompt)  # Ask again
    return value

plainText = get_valid_16bit_input("Enter a 16-bit binary plaintext: ")
key = get_valid_16bit_input("Enter a 16-bit binary key: ")
IV = get_valid_16bit_input("Enter a 16-bit binary IV: ")

def apply_sBox(block, sBox):
    substituted = ""
    for i in range(0, 16, 4):
        index = int(block[i:i+4], 2)
        substituted += format(sBox[index], '04b')
    return substituted

def apply_XOR(block1, block2):
    result = ""
    for i in range(16):
        bit1 = int(block1[i])  # Convert character '0' or '1' to integer (0 or 1)
        bit2 = int(block2[i])  # Convert character '0' or '1' to integer (0 or 1)
        xor_bit = bit1 ^ bit2   # Perform XOR operation (1 if bits are different, 0 if same)
        result += str(xor_bit)  # Convert XOR result back to string and add to result

    return result  # Return the final XOR result (16-bit binary string)


def apply_pBox(block, pBox):
    permuted = ""
    for i in pBox:
        permuted += block[i]
    return permuted  # Return the final permuted 16-bit binary string

def cbc_encrypt(plaintext, key, IV, sBox, pBox):
    ciphertext_blocks = []
    prev_ciphertext = IV

    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]

        xor_result = apply_XOR(block, prev_ciphertext)
        substituted = apply_sBox(xor_result, sBox)
        ciphertext = apply_pBox(substituted, pBox)

        ciphertext_blocks.append(ciphertext)
        prev_ciphertext = ciphertext

    return "".join(ciphertext_blocks)

def cbc_decrypt(ciphertext, key, IV, inverse_sBox, inverse_pBox):
    decrypted_blocks = []
    prev_ciphertext = IV

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]

        pbox_reversed = apply_pBox(block, inverse_pBox)
        sbox_reversed = apply_sBox(pbox_reversed, inverse_sBox)
        decrypted_block = apply_XOR(sbox_reversed, prev_ciphertext)

        decrypted_blocks.append(decrypted_block)
        prev_ciphertext = block

    return "".join(decrypted_blocks)

ciphertext = cbc_encrypt(plainText, key, IV, sBox, pBox)
print("Ciphertext:", ciphertext)

decrypted_text = cbc_decrypt(ciphertext, key, IV, inverse_sBox, inverse_pBox)
print("Decrypted:", decrypted_text)