"""
TUGAS MINI - VIGENÈRE CIPHER
Program enkripsi dan dekripsi otomatis dengan output ke file
"""

def vigenere_encrypt(plaintext, key):
    """Enkripsi teks menggunakan Vigenère Cipher"""
    key = key.upper()
    result = ""
    key_index = 0
    
    for char in plaintext.upper():
        if char.isalpha():
            # Hitung shift dari karakter kunci
            shift = ord(key[key_index % len(key)]) - 65
            # Enkripsi karakter
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result += encrypted_char
            key_index += 1
        else:
            result += char
    
    return result

def vigenere_decrypt(ciphertext, key):
    """Dekripsi teks menggunakan Vigenère Cipher"""
    key = key.upper()
    result = ""
    key_index = 0
    
    for char in ciphertext.upper():
        if char.isalpha():
            # Hitung shift dari karakter kunci (negatif untuk dekripsi)
            shift = ord(key[key_index % len(key)]) - 65
            # Dekripsi karakter
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            result += decrypted_char
            key_index += 1
        else:
            result += char
    
    return result

def main():
    print("=" * 50)
    print("🔐 PROGRAM VIGENÈRE CIPHER")
    print("=" * 50)
    
    # Input dari user
    text = input("Masukkan teks: ")
    key = input("Masukkan kunci (kata/huruf): ")
    
    # Validasi key (hanya huruf)
    if not key.isalpha():
        print("❌ Error: Kunci harus berupa huruf saja!")
        return
    
    # Proses enkripsi dan dekripsi
    enc = vigenere_encrypt(text, key)
    dec = vigenere_decrypt(enc, key)
    
    # Tampilkan hasil
    print("\n" + "=" * 50)
    print("📊 HASIL")
    print("=" * 50)
    print(f"Teks Asli       : {text.upper()}")
    print(f"Hasil Enkripsi  : {enc}")
    print(f"Hasil Dekripsi  : {dec}")
    print(f"Kunci           : {key.upper()}")
    print("=" * 50)
    
    # Simpan ke file
    filename = "hasil_vigenere_cipher.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("HASIL PROGRAM VIGENÈRE CIPHER\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Teks Asli       : {text.upper()}\n")
        f.write(f"Hasil Enkripsi  : {enc}\n")
        f.write(f"Hasil Dekripsi  : {dec}\n")
        f.write(f"Kunci           : {key.upper()}\n")
        f.write("\n" + "=" * 50 + "\n")
    
    print(f"\n✅ Hasil telah disimpan ke file: {filename}")

if __name__ == "__main__":
    main()