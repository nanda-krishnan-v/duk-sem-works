import oqs

# Initialize Kyber-512 KEM
kem = oqs.KeyEncapsulation('Kyber512')

# Generate key pair (recipient side)
public_key = kem.generate_keypair()
print(f"Public key length: {len(public_key)} bytes")

# Sender encapsulates shared secret using recipient's public key
ciphertext, shared_secret_sender = kem.encap_secret(public_key)
print(f"Ciphertext length: {len(ciphertext)} bytes")
print(f"Shared secret (sender): {shared_secret_sender.hex()}")

# Recipient decapsulates to retrieve shared secret
shared_secret_recipient = kem.decap_secret(ciphertext)
print(f"Shared secret (recipient): {shared_secret_recipient.hex()}")

# Verify both parties have the same shared secret
if shared_secret_sender == shared_secret_recipient:
    print("✓ Success: Both sender and recipient derived the same secret key")
else:
    print("✗ Error: Secret keys do not match")

print(f"\nShared secret length: {len(shared_secret_sender)} bytes")