def KeySchAlgo(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, text_length):
    i = j = 0
    keystream = []
    for _ in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream.append(S[(S[i] + S[j]) % 256])
    return keystream

def generate_keystream(key, text_length):
    key = [ord(c) for c in key]
    S = KeySchAlgo(key)
    return PRGA(S, text_length)

def RC4_encrypt(key, plaintext):
    keystream = generate_keystream(key, len(plaintext))
    return bytes([plaintext[i] ^ keystream[i] for i in range(len(plaintext))])

def RC4_decrypt(key, ciphertext):
    return RC4_encrypt(key, ciphertext)  # XORing again restores the original text

key = input("Enter the encryption key: ")
plaintext = input("Enter the plaintext: ").encode()
ciphertext = RC4_encrypt(key, plaintext)
decrypted_text = RC4_decrypt(key, ciphertext)

print("\nCiphertext (Hex):", ciphertext.hex())
print("Decrypted Text:", decrypted_text.decode())