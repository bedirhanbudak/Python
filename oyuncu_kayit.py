print("Oyuncu Kayıt Programına Hoş Geldiniz! \n Program başlatılıyor...")


a = str(input("1. Oyuncunun İsmini Giriniz: "))
b = str(input("2. Oyuncunun İsmini Giriniz: "))
c = str(input("3. Oyuncunun İsmini Giriniz: "))


oyuncular = [a,b,c]

print("Veriler Kaydedildi!")

print("İlk oyuncu: {}\nİkinci oyuncu: {}\nÜçüncü oyuncu: {}".format(oyuncular[0],oyuncular[1],oyuncular[2]))