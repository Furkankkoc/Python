faktoriyel = 1

while True:
    sayi = int(input("negatif olmayan bir sayı giriniz :"))
    if sayi <= 0:
        print("negatif olmayan bir sayı giriniz")

    else:
        for i in range(1, sayi + 1):
            faktoriyel *= i

        print("faktoriyel", faktoriyel)
        break
