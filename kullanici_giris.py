"""
Kullanıcı adı: bedirhan
Parola: budak
"""

print("Giriş yapmak için kullanıcı adı ve parola girmelisiniz")

while True:

    k_adi = input("Kullanıcı adı: ")
    sifre = input("Şifre: ")

    if k_adi == "bedirhan" and sifre != "budak":
        print("Yanlış şifre!")
    elif k_adi != "bedirhan" and sifre == "budak":
        print("Böyle bir kullanıcı yok!")
    elif k_adi != "bedirhan" and sifre != "budak":
        print("Kullanıcı adı ve şifre hatalı!")
    else:
        print("Giriş Başarılı...")
        break