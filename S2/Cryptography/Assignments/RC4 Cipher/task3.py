
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


def bitwise_difference(a, b):
    return sum(bin(x ^ y).count('1') for x, y in zip(a, b))

key = input("Enter the encryption key: ")
plaintext = input("Enter the plaintext: ").encode()
ciphertext = RC4_encrypt(key, plaintext)
decrypted_text = RC4_decrypt(key, ciphertext)

print("\nCiphertext:", ciphertext.hex())
print("Decrypted Text:", decrypted_text.decode())

#Effect of Plaintext Variations
print("\nTask 3: Effect of Plaintext Variations")
plaintext_variation = input("Enter a slightly modified plaintext: ").encode()
ciphertext_variation = RC4_encrypt(key, plaintext_variation)

print("Ciphertext for Original Plaintext:", ciphertext.hex())
print("Ciphertext for Modified Plaintext:", ciphertext_variation.hex())
bit_diff_plaintext = bitwise_difference(ciphertext, ciphertext_variation)
print(f"Bitwise difference between ciphertexts due to plaintext variation: {bit_diff_plaintext} bits")
