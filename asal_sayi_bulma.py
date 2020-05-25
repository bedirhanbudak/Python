#Geliştirilebilir

def asal(sayi = 0):
    while True:
        sayi = int(input("Sayıyı girin: "))
        if sayi > 1 and sayi != 2:
            for i in range(2, sayi):

                if sayi%i == 0:
                    print("Asal değil")
                    break
                else:
                    print("Asal sayı")
                    break

        elif sayi == 1:
            print("Asal değil")
        elif sayi == 2:
            print("Asal sayı")
        else:
            print("Hatalı sorgulama!")

asal()