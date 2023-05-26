liczby = [56,1009,-999,0,113,467,-237,888,23,9,-4,-55,876,-555,98,12,34,117,700]

def statystyki_listy(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    liczbael = len(lista)
    sumael = sum(lista)
    sr_arytm = sumael/liczbael
    return minimum,maksimum,rozstep,liczbael,sumael,sr_arytm

wynik = statystyki_listy(liczby)
print(wynik)
print(type(wynik))

mini, maxi, roz, le, se, sa = statystyki_listy(liczby)
print(f"wartość największa: {maxi}, wartość najmniejsza: {mini}, rozstęp: {roz}, liczba elemenetów: {le},\n "
      f"suma elementów: {se}, średnia arytmetyczna: {sa:.2f}")
