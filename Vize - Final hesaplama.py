a = int(input("vize puanı giriniz"))
b = int(input("final puanı giriniz"))

ortalama = a * 0.4 + b * 0.6

if ortalama >= 50:
    print("dersi geçtiniz")

else:
    print("dersten kaldınız")
