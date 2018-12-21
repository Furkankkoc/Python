a = int(input("birincisayi"))
b = int(input("ikincisayi"))
c = int(input("ücüncüsayi"))
d = int(input("dördüncüsayi"))
e = int(input("besincisayi"))

dizi = [a,b,c,d,e]

dizi.sort(reverse = True)
print(dizi)
algoritma = str(dizi)
dosya = open("C:\ogrencino_sonuc.txt", "w")
dosya.write(algoritma)
dosya.close()
