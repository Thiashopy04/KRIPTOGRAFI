# ds_demo.py — gabungan hash + RSA signing
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# generate keys
key = RSA.generate(2048)
priv = key.export_key()
pub = key.publickey().export_key()

message = b'saya thia dan saya bangga menjadi fans emyu'
hash_obj = SHA256.new(message)

# sign
signature = pkcs1_15.new(RSA.import_key(priv)).sign(hash_obj)

# verify
try:
    pkcs1_15.new(RSA.import_key(pub)).verify(hash_obj, signature)
    verified = True
except (ValueError, TypeError):
    verified = False

print('Signature length:', len(signature))
print('Verified:', verified)
