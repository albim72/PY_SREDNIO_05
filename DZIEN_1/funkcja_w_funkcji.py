import math
import time

def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik: {imie}, zdobyte punkty: {punkty}"

def f(x):
    return math.sqrt(x-2)

def info():
    return "ważna informacja"

def osoba(funkcja,*atr):
    print(f"uruchamiam funkcję {funkcja.__name__}")
    time.sleep(3)
    return funkcja(*atr)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Anna",78))
print(osoba(f,67))
print(osoba(info))

#prosty dekorator

def nowafunkcja(funkcja)

