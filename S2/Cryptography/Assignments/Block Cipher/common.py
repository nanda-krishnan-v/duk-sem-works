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

def ecb_encrypt():
    plaintext = input("Enter a 16-bit binary plaintext: ")
    key = input("Enter a 16-bit binary key: ")
    ciphertext = ""
    for c in plaintext:
        ciphertext += chr(ord(c) + int(key))
    print("Ciphertext:", ciphertext)

def ecb_decrypt():
    ciphertext = input("Enter the ciphertext: ")
    key = input("Enter the key: ")
    decrypted_text = ""
    for c in ciphertext:
        decrypted_text += chr(ord(c) - int(key))
    print("Decrypted:", decrypted_text.rstrip())

def cbc_encrypt():
    plaintext = input("Enter a 16-bit binary plaintext: ")
    key = input("Enter a 16-bit binary key: ")
    IV = input("Enter a 16-bit binary IV: ")
    print("CBC encryption not implemented yet.")

def cbc_decrypt():
    ciphertext = input("Enter the ciphertext: ")
    key = input("Enter the key: ")
    IV = input("Enter a 16-bit binary IV: ")
    print("CBC decryption not implemented yet.")

def cfb_encrypt():
    plaintext = input("Enter a 16-bit binary plaintext: ")
    key = input("Enter a 16-bit binary key: ")
    IV = input("Enter a 16-bit binary IV: ")
    print("CFB encryption not implemented yet.")

def cfb_decrypt():
    ciphertext = input("Enter the ciphertext: ")
    key = input("Enter the key: ")
    IV = input("Enter a 16-bit binary IV: ")
    print("CFB decryption not implemented yet.")

def main():
    mode = input("Select mode (ECB/CBC/CFB): ").strip().lower()
    if mode == "ecb":
        action = input("Select action (encrypt/decrypt): ").strip().lower()
        if action == "encrypt":
            ecb_encrypt()
        elif action == "decrypt":
            ecb_decrypt()
        else:
            print("Invalid action selected!")
    elif mode == "cbc":
        action = input("Select action (encrypt/decrypt): ").strip().lower()
        if action == "encrypt":
            cbc_encrypt()
        elif action == "decrypt":
            cbc_decrypt()
        else:
            print("Invalid action selected!")
    elif mode == "cfb":
        action = input("Select action (encrypt/decrypt): ").strip().lower()
        if action == "encrypt":
            cfb_encrypt()
        elif action == "decrypt":
            cfb_decrypt()
        else:
            print("Invalid action selected!")
    else:
        print("Invalid mode selected!")

if __name__ == "__main__":
    main()
