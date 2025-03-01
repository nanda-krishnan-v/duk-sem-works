sBox = {
    0: 14, 1: 4, 2: 13, 3: 1,
    4: 2, 5: 15, 6: 11, 7: 8,
    8: 3, 9: 10, 10: 6, 11: 12,
    12: 5, 13: 9, 14: 0, 15: 7
}
pBox = [15, 0, 8, 7, 12, 3, 9, 5, 6, 1, 10, 4, 2, 14, 13, 11]

def get_valid_16bit_input(prompt):
    value = input(prompt)
    while len(value) != 16 or any(c not in '01' for c in value):
        value = input("Invalid input! " + prompt)  
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
    return "".join(str(int(block1[i]) ^ int(block2[i])) for i in range(16))

def apply_pBox(block, pBox):
    return "".join(block[i] for i in pBox)

def cfb_encrypt(plaintext, key, IV, sBox, pBox):
    ciphertext_blocks = []
    prev_ciphertext = IV  

    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]  

        encrypted_IV = apply_pBox(apply_sBox(prev_ciphertext, sBox), pBox)
        ciphertext = apply_XOR(block, encrypted_IV)  

        ciphertext_blocks.append(ciphertext)  
        prev_ciphertext = ciphertext  

    return "".join(ciphertext_blocks)

def cfb_decrypt(ciphertext, key, IV, sBox, pBox):
    decrypted_blocks = []
    prev_ciphertext = IV  

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]  

        encrypted_IV = apply_pBox(apply_sBox(prev_ciphertext, sBox), pBox)
        decrypted_block = apply_XOR(block, encrypted_IV)  

        decrypted_blocks.append(decrypted_block)  
        prev_ciphertext = block  

    return "".join(decrypted_blocks)

ciphertext = cfb_encrypt(plainText, key, IV, sBox, pBox)
print("Ciphertext:", ciphertext)

decrypted_text = cfb_decrypt(ciphertext, key, IV, sBox, pBox)
print("Decrypted:", decrypted_text)
