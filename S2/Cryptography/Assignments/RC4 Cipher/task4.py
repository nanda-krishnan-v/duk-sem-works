import math
from collections import Counter
import time 

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

def measure_time(func, key, text):
    start_time = time.time()
    func(key, text)
    return time.time() - start_time

def calculate_entropy(data):
    frequency = Counter(data)
    probabilities = [count / len(data) for count in frequency.values()]
    return -sum(p * math.log2(p) for p in probabilities)

def measure_time(func, key, text):
    start_time = time.time()
    func(key, text)
    return time.time() - start_time

key = input("Enter an 8-character key: ")
if len(key) != 8:
    print("Key must be exactly 8 characters.")
    exit()

for _ in range(3):
    size = int(input("Enter plaintext size: "))
    plaintext = input(f"Enter plaintext of size {size}: ")
    if len(plaintext) != size:
        print(f"Error: Plaintext must be exactly {size} characters.")
        exit()

    plaintext_encoded = plaintext.encode()
    encryption_time = measure_time(RC4_encrypt, key, plaintext_encoded)
    ciphertext = RC4_encrypt(key, plaintext_encoded)
    entropy = calculate_entropy(ciphertext)

    print(f"\nPlaintext Size: {size} bytes")
    print(f"Ciphertext: {ciphertext.hex()}")
    print(f"Entropy: {entropy:.4f}")
    print(f"Encryption Time: {encryption_time:.6f} seconds")
