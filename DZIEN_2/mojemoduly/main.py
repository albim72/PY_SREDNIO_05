#import dane
#import dane as dn
from dane import nrfilii as filia
from dane import book as ks

from bfunkcje.kol_funkcje import czytaj_liste,czytaj_slownik

from bklasy.klasa_dane import CDane

print("_"*15,"dane bezpośrednie","_"*15)
print(filia)
print(ks)

print("_"*15,"dane z funkcji","_"*15)
czytaj_liste(filia)
czytaj_slownik(ks)

print("_"*15,"dane z klasy","_"*15)
cd = CDane(filia,ks)
cd.czytaj_l()
cd.czytaj_s()
