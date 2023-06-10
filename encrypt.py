from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(knock_sequence, key):
    cipher = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
    ciphertext = cipher.encrypt(pad(knock_sequence.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt(encrypted_sequence, key):
    iv = encrypted_sequence[:16]
    ciphertext = encrypted_sequence[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_sequence = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_sequence.decode()

# Contoh penggunaan
key = get_random_bytes(16)  # Generate kunci enkripsi

# Enkripsi knock sequence
knock_sequence = "7000 8000 9000"
encrypted_sequence = encrypt(knock_sequence, key)
print("Encrypted Sequence:", encrypted_sequence.hex())

# Dekripsi knock sequence
decrypted_sequence = decrypt(encrypted_sequence, key)
print("Decrypted Sequence:", decrypted_sequence)