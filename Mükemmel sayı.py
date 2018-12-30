toplam = 0

a = int(input("bir sayı giriniz"))

for i in range(1,a):
    if a % i == 0:
        toplam += i

if toplam == a:
    print("mükemmel sayı")

else:
    print("sayı mükemmel değil")
