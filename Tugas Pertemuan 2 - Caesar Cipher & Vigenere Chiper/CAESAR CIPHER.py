"""
TUGAS MINI - CAESAR CIPHER
Program enkripsi dan dekripsi otomatis dengan output ke file
"""

def caesar_encrypt(text, shift):
    """Enkripsi teks menggunakan Caesar Cipher"""
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """Dekripsi teks menggunakan Caesar Cipher"""
    return caesar_encrypt(text, -shift)

def main():
    print("=" * 50)
    print("🔐 PROGRAM CAESAR CIPHER")
    print("=" * 50)
    
    # Input dari user
    text = input("Masukkan teks: ")
    shift = int(input("Masukkan shift (1-25): "))
    
    # Proses enkripsi dan dekripsi
    enc = caesar_encrypt(text, shift)
    dec = caesar_decrypt(enc, shift)
    
    # Tampilkan hasil
    print("\n" + "=" * 50)
    print("📊 HASIL")
    print("=" * 50)
    print(f"Teks Asli       : {text.upper()}")
    print(f"Hasil Enkripsi  : {enc}")
    print(f"Hasil Dekripsi  : {dec}")
    print(f"Shift           : {shift}")
    print("=" * 50)
    
    # Simpan ke file
    filename = "hasil_caesar_cipher.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("HASIL PROGRAM CAESAR CIPHER\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Teks Asli       : {text.upper()}\n")
        f.write(f"Hasil Enkripsi  : {enc}\n")
        f.write(f"Hasil Dekripsi  : {dec}\n")
        f.write(f"Shift           : {shift}\n")
        f.write("\n" + "=" * 50 + "\n")
    
    print(f"\n✅ Hasil telah disimpan ke file: {filename}")

if __name__ == "__main__":  # ✅ PERBAIKAN: double underscore
    main()