while True:
    sayi = int(input("Faktöriyelini hesaplamak istedğiniz sayıyı giriniz:\n"))
    if sayi == 0:
        print("Sayının faktöriyeli: 1")
    elif sayi > 0:
        f = range(1, sayi+1)
        for i in f:
            i *= i
        print("Sayının faktöriyeli: {}".format(i))
    else:
        print("Pozitif bir tamsayı girmelisiniz!")