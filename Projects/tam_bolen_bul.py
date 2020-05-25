def tam_bolen(sayi):
    liste = []
    for i in range(2 , sayi):
        if sayi % i == 0:
            liste.append(i)
    return liste

while True:

    sayi = input("Sayı girin: ")
    if sayi == "q":
        break
    else:
        sayi = int(sayi)
        print("Tam bölenler:", tam_bolen(sayi))
