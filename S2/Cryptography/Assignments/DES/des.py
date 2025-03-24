from Crypto.Cipher import DES # type: ignore
from Crypto.Random import get_random_bytes # type: ignore
import time

def pad(text):
    padding_length = 8 - (len(text) % 8)
    return text + bytes([padding_length] * padding_length)

def unpad(text):
    return text[:-text[-1]]

key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"Hello, DES"
padded_text = pad(plaintext)

start_enc = time.time()
ciphertext = cipher.encrypt(padded_text)
end_enc = time.time()

decipher = DES.new(key, DES.MODE_ECB)
start_dec = time.time()
decrypted = unpad(decipher.decrypt(ciphertext))
end_dec = time.time()

print("Encrypted:", ciphertext)
print("Decrypted:", decrypted.decode())
print("Encryption time:", end_enc - start_enc)
print("Decryption time:", end_dec - start_dec)