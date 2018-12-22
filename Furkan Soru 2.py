a = input("cümle gir")
print(a[::-1])
print(a.split(" "))
h = []
s = []
for i in(a):
    if not (i in h):
        h.append(i)
        s.append(1)
    else:
        s[h.index(i)] = s[h.index(i)] + 1
print("harflerin sayısı")
for j in range(len(h)):
    print(h[j], "=", s[j], "tane")

tersten = a[::-1]
bolunenler = tersten.split(" ")
print("Kelimeleri kendi içinde ters çevirme", bolunenler[::-1])

unluharfler = ["a","e","o","ö","u","ü","ı","i"]
unlu = []
unsuz = []

for i in a:
    if i == unluharfler[0]or i == unluharfler[1]or i == unluharfler[2]or i == unluharfler[3]or i == unluharfler[4]or i == unluharfler[5]or i == unluharfler[6]or i == unluharfler[7]:
        unlu.append(i)
    else:
        unsuz.append(i)
print("Ünlüler", unlu)
print("Ünsüzler", unsuz)




