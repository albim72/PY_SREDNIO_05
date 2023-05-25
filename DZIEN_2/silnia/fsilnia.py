#n! = 1*2*3*...*n
#double -> 1.8E+308
#n??? 171!


def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik
