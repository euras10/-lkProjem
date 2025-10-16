#!/usr/bin/env python3
import secrets
import string

def get_bool(prompt):
    while True:
        resp = input(prompt + " (E/H): ").strip().lower()
        if resp in ("e", "evet", "y", "yes"):
            return True
        if resp in ("h", "hayır", "hayir", "n", "no"):
            return False
        print("Geçersiz giriş — evet için 'E', hayır için 'H' gir.")

def main():
    print("== Güvenli Rastgele Şifre Oluşturucu ==")
    try:
        length = int(input("Şifre uzunluğu (örn. 12): ").strip())
        if length <= 0:
            print("Uzunluk pozitif bir sayı olmalı.")
            return
    except ValueError:
        print("Geçersiz sayı.")
        return

    # Ana karakter seçimleri
    use_lower = get_bool("Küçük harf olsun mu")
    use_upper = get_bool("Büyük harf olsun mu")
    use_digits = get_bool("Rakam olsun mu")
    use_symbols = get_bool("Sembol (örn. !@#) olsun mu")

    # Ek seçenekler
    exclude_similar = get_bool("Benzer karakterleri hariç tut (örn. 0/O, 1/l)")
    include_space = get_bool("Boşluk karakteri eklensin mi")
    save_to_file = get_bool("Oluşturulan şifreyi 'sifre.txt' dosyasına kaydetmek ister misin")

    # Karakter seti oluştur
    alphabet = ""
    if use_lower:  alphabet += string.ascii_lowercase
    if use_upper:  alphabet += string.ascii_uppercase
    if use_digits: alphabet += string.digits
    if use_symbols: alphabet += string.punctuation
    if include_space: alphabet += " "

    if exclude_similar:
        for ch in "0O1lI":
            alphabet = alphabet.replace(ch, "")

    if not alphabet:
        print("En az bir karakter türü seçmelisin.")
        return

    # Şifre oluşturma
    password_chars = []
    if use_lower:  password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_upper:  password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_digits: password_chars.append(secrets.choice(string.digits))
    if use_symbols: password_chars.append(secrets.choice(string.punctuation))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(alphabet))

    secrets.SystemRandom().shuffle(password_chars)
    password = ''.join(password_chars[:length])

    print("\nOluşturulan şifre:", password)

    if save_to_file:
        with open("sifre.txt", "w", encoding="utf-8") as f:
            f.write(password)
        print("✅ Şifre 'sifre.txt' dosyasına kaydedildi!")

if __name__ == "__main__":
    main()