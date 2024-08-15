import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while True:
    sayi = int(input("Kaç karakterlik şifre istersiniz?"))

    password = ""
    for i in range(sayi):
            password += random.choice(karakterler)


    print("Şifreniz=", password)