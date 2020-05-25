import random
import time

print(""""
***********************************
Sayı tahmin oyunununa hoş geldiniz.
***********************************
""")

sayi = random.randint(1, 20)

def yardim():
    while True:
        tahmin = int(input("1 ile 20 arasında bir tahmin yapınız: "))
        if tahmin < sayi:
            print("Daha büyük bir sayı girin.")
        elif tahmin > sayi:
            print("Daha küçük bir sayı girin.")
        else:
            print("Tebribkler, sayıyı buldunuz. Sayı:{} ".format(sayi))
            break
yardim()