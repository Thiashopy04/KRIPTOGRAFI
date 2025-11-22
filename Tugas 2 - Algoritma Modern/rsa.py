from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate keys
key = RSA.generate(2048)
private_key_pem = key.export_key()
public_key_pem = key.publickey().export_key()

# Encrypt / Decrypt (OAEP)
def rsa_encrypt(message: bytes, pub_pem: bytes) -> bytes:
    pub = RSA.import_key(pub_pem)
    cipher = PKCS1_OAEP.new(pub)
    return cipher.encrypt(message)

def rsa_decrypt(ciphertext: bytes, priv_pem: bytes) -> bytes:
    priv = RSA.import_key(priv_pem)
    cipher = PKCS1_OAEP.new(priv)
    return cipher.decrypt(ciphertext)

# Sign / Verify (PKCS#1 v1.5)
def rsa_sign(message: bytes, priv_pem: bytes) -> bytes:
    priv = RSA.import_key(priv_pem)
    h = SHA256.new(message)
    signature = pkcs1_15.new(priv).sign(h)
    return signature

def rsa_verify(message: bytes, signature: bytes, pub_pem: bytes) -> bool:
    pub = RSA.import_key(pub_pem)
    h = SHA256.new(message)
    try:
        pkcs1_15.new(pub).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# Contoh penggunaan
if __name__ == '__main__':
    msg = b'hello RSA'
    
    ct = rsa_encrypt(msg, public_key_pem)
    pt = rsa_decrypt(ct, private_key_pem)
    
    sig = rsa_sign(msg, private_key_pem)
    ok = rsa_verify(msg, sig, public_key_pem)

    print('Decrypted:', pt)
    print('Signature valid?', ok)
