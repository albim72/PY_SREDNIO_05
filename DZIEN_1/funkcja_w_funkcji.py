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

def nowafunkcja(funkcja):
    def wrapper(*args):
        print(f"Uruchomienie funkcji: {funkcja.__name__}")
        ts = time.perf_counter()
        print(funkcja(*args))
        tk = time.perf_counter()
        print(f"zakończenie pracy funkcji: {funkcja.__name__}")
        print(f"czas wykonania funkcji: {tk-ts} s")
    return wrapper

def policz(a,b):
    n = sum([(a+n)**b for n in range(350_000)])
    return n

wyn = nowafunkcja(policz)
wyn(2,3)

@nowafunkcja
def policz_2(a,b,c):
    n = sum([(a/c+n)**b for n in range(990_000)])
    return n


policz_2(2,6,1)

