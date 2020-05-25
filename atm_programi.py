print("""
***Hoşgeldiniz***

Bakiye sorgulamak için: 1

Para yatırmak için: 2

Para çekmek için: 3

""")

bakiye = 500
islem = 0
para_yatirma = 0
para_cekme = 0

while islem != "q":

    islem = input('Yapmak istediğiniz işlemin numarasını yazın.\nÇıkmak için "q" yazın.\n')

    if islem == "q":
        print("Çıkış yapılıyor...")

    elif islem == "1":
        print("Bakiyeiz:{} ".format(bakiye))

    elif islem == "2":
        while True:
            para_yatirma = int(input("Yatırmak istediğiniz miktarı giriniz (TL): "))
            if para_yatirma >= 0:
                print("Para yatırılıyor, lütfen bekleyiniz.")
                bakiye += para_yatirma
                print("İşlem başarılı")
                break
            else:
                print("Geçersiz miktar girdiniz. Tekrar giriniz.")

    elif islem == "3":
        while True:
            para_cekme = int(input("Çekmek istediğiniz miktarı giriniz (TL): "))
                if para_cekme >= 0:
                    print("İşleminiz yapılıyor, lütfne bekleyiniz.")
                    bakiye -= para_cekme
                    print("İşlem başarılı")
                    break
                elif para_cekme > bakiye:
                    print("Yetersiz bakiye!")
                    break
                else:
                print("Geçersiz miktar girdiniz. Tekrar giriniz.")
            else:
                print("Geçersiz miktar girdiniz. Tekrar giriniz.")

    else:
        print("Hatalı bir işlem yaptınız, lütfen tekrar deneyin.")
