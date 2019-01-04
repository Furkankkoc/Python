a = int(input("sayı giriniz"))
for i in range(100,1000):

    ilkrakam = a // 100
    ikincirakam = a % 100 // 10
    ucuncurakam = a % 10
    
    islem = (ilkrakam * ikincirakam * ucuncurakam) % (ilkrakam + ikincirakam + ucuncurakam)

print("islem:", islem)
