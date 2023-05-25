from pojazd import Pojazd

poj = Pojazd()
odl = float(input("podaj odległość [km]: "))
lt = float(input("podaj liczbę spalonych litrów paliwa [l]: "))
cn = float(input("podaj cenę paliwa za litr [zł]: "))
print(f"spalanie [l/100km]: {poj.spal_100(odl,lt):.2f}")
print(f"koszt przejazdu na trasie {odl} km wynosi {poj.kosztyprzejazdu(odl,lt,cn):.2f} zł")
