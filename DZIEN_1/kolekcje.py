print("pierwsza linia na dobry początek")

#komentarz podstawowy - jednoliniowy
"""
komentarz wieloliniowy
"""

kom = """
drugi
komentarz
"""

txt = "jfkdjfk l;fsdldfksdl"

print(kom)

a:int = True

print(a)
print(type(a))

a = "jedynka"

print(a)
print(type(a))

#cztery podstawowe kolekcje: listy, krotki, zbiory i słowniki

imiona = ["Jan","Piotr","Anna","Kinga","Henryk","Leon","Nadia","Anna","Jan"]
imiona_tp = ("Jan","Piotr","Anna","Kinga","Henryk","Leon","Nadia","Anna","Jan")

print(imiona)
print(type(imiona))

print(imiona_tp)
print(type(imiona_tp))

print(imiona[2:4])
print(imiona_tp[2:4])

imiona.append("Marek")
#krotka to lista niemutowalna

w = "kalejdoskop"
print(w)
print(w[0])
print(w[1])
print(w[2:6])
print(w[:5])
print(w[1:])
print(w[-1])
print(w[2:8:2])
print(w[::2])

print(w[::-1])

kolory = {"zielony","czerwony","biały","żółty","niebieski","zielony"}
print(kolory)
print(kolory)
print(kolory)
print(type(kolory))
ekstra = ["szary","czarny","navy"]
kolory.update(ekstra)
print(kolory)

listakol = list(kolory)
print(listakol)
listatp = tuple(kolory)
print(listatp)

osoba = {
    "imie":"Jan",
    "nazwisko":"Kot",
    "miasto":"Kraków",
    "wiek":44
}

#słownik -> asocjacja (klucz,wartość)

print(osoba)
print(osoba["miasto"])

print("___klucze____")
for x in osoba:
    print(x)

print("___klucze____")
for x in osoba.keys():
    print(x)


print("___wartości____")
for x in osoba:
    print(osoba[x])

print("___wartości2____")
for x in osoba.values():
    print(x)

print("___items(pary)____")
for x,y in osoba.items():
    print(f"{x}: {y}")


osoby = ["Jan","Piotr","Anna","Kinga","Henryk","Leon","Nadia","Anna","Jan"]

print(list(enumerate(osoby)))

for i,os in enumerate(osoby):
    print(i,os)








