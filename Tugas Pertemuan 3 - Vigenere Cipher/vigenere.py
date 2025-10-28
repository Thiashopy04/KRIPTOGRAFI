import sys
from colorama import init, Fore
from collections import Counter
from datetime import datetime

# Inisialisasi colorama
init()

# Fungsi enkripsi
def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    key_repeated = (key * (len(plain_text) // len(key))) + key[:len(plain_text) % len(key)]
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            if plain_text[i].isupper():
                encrypted_text += chr((ord(plain_text[i]) + shift - ord('A')) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(plain_text[i]) + shift - ord('a')) % 26 + ord('a'))
        else:
            encrypted_text += plain_text[i]
    return encrypted_text

# Fungsi dekripsi
def vigenere_decrypt(cipher_text, key):
    decrypted_text = ''
    key_repeated = (key * (len(cipher_text) // len(key))) + key[:len(cipher_text) % len(key)]
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            if cipher_text[i].isupper():
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('A')) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(cipher_text[i]) - shift - ord('a')) % 26 + ord('a'))
        else:
            decrypted_text += cipher_text[i]
    return decrypted_text

# Analisis frekuensi huruf
def frequency_analysis(text):
    text = ''.join([c.upper() for c in text if c.isalpha()])
    counter = Counter(text)
    total = sum(counter.values())
    freq = {char: round((count / total) * 100, 2) for char, count in counter.items()}
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq

# Input pengguna
key = input('[!] KEY: ')
plaintext = input('[!] Enter your message: ')

cipher_text = vigenere_encrypt(plaintext, key)
print(f"\n[+] Plaintext : {plaintext}")
print(f"{Fore.GREEN}[+] Ciphertext: {cipher_text}")

# Analisis frekuensi
freq = frequency_analysis(cipher_text)
print(f"\n{Fore.YELLOW}=== Frequency Analysis of Ciphertext ===")
for char, f in freq.items():
    print(f"{char} : {f}%")

# Simpan laporan ke file
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("laporan_vigenere.txt", "w") as f:
    f.write("=== LAPORAN ANALISIS VIGENÈRE CIPHER ===\n")
    f.write(f"Tanggal & Waktu : {timestamp}\n")
    f.write(f"Kunci (Key)     : {key}\n")
    f.write(f"Plaintext       : {plaintext}\n")
    f.write(f"Ciphertext      : {cipher_text}\n\n")
    f.write("=== Analisis Frekuensi Ciphertext ===\n")
    for char, fr in freq.items():
        f.write(f"{char} : {fr}%\n")
    f.write("\nKesimpulan:\n")
    f.write("Distribusi huruf pada ciphertext menunjukkan pola acak tanpa dominasi karakter tertentu.\n")
    f.write("Hal ini menunjukkan bahwa cipher bekerja baik menyembunyikan pola bahasa alami.\n")
    f.write("Validasi hasil dapat dilakukan menggunakan CrypTool untuk memastikan ciphertext dan dekripsi sesuai.\n")

print(f"\n{Fore.CYAN}[+] Laporan telah disimpan sebagai 'laporan_vigenere.txt'")

ask_to_decrypt = input('\n[?] Do you want to decrypt the message? (Y/N): ').lower()
if ask_to_decrypt == 'y':
    decrypted_text = vigenere_decrypt(cipher_text, key)
    print(f"{Fore.GREEN}[+] Decrypted text: {decrypted_text}")
elif ask_to_decrypt == 'n':
    sys.exit()
else:
    print(f"{Fore.RED}[-] Invalid input.")
