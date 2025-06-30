from datetime import datetime

def harf_notu(puan):
    if puan >= 90:
        return "AA"
    elif puan >= 80:
        return "BA"
    elif puan >= 70:
        return "BB"
    elif puan >= 60:
        return "CB"
    elif puan >= 50:
        return "CC"
    elif puan >= 40:
        return "DC"
    elif puan >= 30:
        return "DD"
    else:
        return "FF"

def notlari_hesapla():
    sayi = int(input("Not hesaplamak istediğiniz öğrenci sayısını girin: "))
    print(f"{sayi} öğrencinin not ortalaması hesaplanacak.")

    toplam = 0
    gecerli_ogrenci = 0

    now = datetime.now()
    tarih = now.strftime("%Y-%m-%d_%H-%M")
    dosya_adi = f"notlar_{tarih}.txt"

    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        for i in range(sayi):
            isim = input(f"{i+1}. öğrencinin ismini girin: ")

            try:
                puan = int(input(f"{isim} adlı öğrencinin notunu girin: "))
                if puan < 0 or puan > 100:
                    print(f"{isim}: Geçersiz not!")
                    dosya.write(f"{isim}: Geçersiz not!\n")
                    continue

                harf = harf_notu(puan)
                toplam += puan
                gecerli_ogrenci += 1

                print(f"{isim}: {puan} → {harf}")
                dosya.write(f"{isim}: {puan} → {harf}\n")

            except ValueError:
                print(f"{isim}: Geçersiz giriş!")
                dosya.write(f"{isim}: Geçersiz giriş!\n")

        if gecerli_ogrenci > 0:
            ortalama = toplam / gecerli_ogrenci
            print("Geçerli öğrenciler için ortalama:", ortalama)
            dosya.write(f"\nSınıf ortalaması: {ortalama}\n")
        else:
            print("Hiç geçerli not girilmedi.")
            dosya.write("\nHiç geçerli not girilmedi.\n")

if __name__ == "__main__":
    notlari_hesapla()