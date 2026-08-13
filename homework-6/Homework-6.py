# 1. 1 dan 10 gacha

son = 1

while son <= 10:
    print(son)
    son += 1


# 2. Juft sonlar

son = 2

while son <= 20:
    print(son, end=" ")
    son += 2


# 3. Sonlar yig'indisi

n = int(input("\nn = "))

son = 1
yigindi = 0

while son <= n:
    yigindi += son
    son += 1

print("Natija:", yigindi)


# 4. Parol tekshirish

parol = "12345"

kiritilgan = input("Parolni kiriting: ")

while kiritilgan != parol:
    kiritilgan = input("Parolni kiriting: ")

print("Kirish muvaffaqiyatli!")


# 5. Bank hisob tizimi

balans = 100000

while True:
    print()
    print("1. Balansni ko'rish")
    print("2. Pul qo'shish")
    print("3. Pul yechish")
    print("4. Chiqish")

    tanlov = int(input("Tanlang: "))

    if tanlov == 1:
        print("Balans:", balans, "so'm")

    elif tanlov == 2:
        pul = int(input("Pul miqdori: "))

        if pul > 0:
            balans += pul
            print("Pul qo'shildi")
        else:
            print("Manfiy pul qo'shib bo'lmaydi")

    elif tanlov == 3:
        pul = int(input("Pul miqdori: "))

        if pul > 0:
            if pul <= balans:
                balans -= pul
                print("Pul yechildi")
            else:
                print("Balansda yetarli mablag' yo'q")
        else:
            print("Manfiy pul yechib bo'lmaydi")

    elif tanlov == 4:
        print("Dastur tugadi!")
        break

    else:
        print("Noto'g'ri tanlov")