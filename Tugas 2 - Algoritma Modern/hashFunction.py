# hash_demo.py
import hashlib


def hash_md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()


def hash_sha1(s: str) -> str:
    return hashlib.sha1(s.encode()).hexdigest()


def hash_sha256(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()


if __name__ == '__main__':
    msg = 'saya thia dan saya bangga menjadi fans emyu'
    print('MD5     :', hash_md5(msg))
    print('SHA-1   :', hash_sha1(msg))
    print('SHA-256 :', hash_sha256(msg))
