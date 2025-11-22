from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

BLOCK_SIZE = 16

def pkcs7_pad(data: bytes) -> bytes:
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len]) * pad_len

def pkcs7_unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        raise ValueError("Invalid padding")
    return data[:-pad_len]

def aes_encrypt(plaintext: str, key: bytes) -> str:
    iv = get_random_bytes(BLOCK_SIZE)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pkcs7_pad(plaintext.encode()))
    return base64.b64encode(iv + ciphertext).decode()

def aes_decrypt(b64_ciphertext: str, key: bytes) -> str:
    raw = base64.b64decode(b64_ciphertext)
    iv = raw[:BLOCK_SIZE]
    ciphertext = raw[BLOCK_SIZE:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    return pkcs7_unpad(decrypted).decode()

# Program utama
if __name__ == "__main__":
    key = get_random_bytes(16)  # AES-128
    message = "saya thia dan saya bangga menjadi fans emyu"

    encrypted = aes_encrypt(message, key)
    decrypted = aes_decrypt(encrypted, key)

    print("Plaintext :", message)
    print("Ciphertext:", encrypted)
    print("Decrypted :", decrypted)
