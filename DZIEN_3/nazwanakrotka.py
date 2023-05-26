from collections import namedtuple

Student = namedtuple('Student',['imie','nazwisko','wiek','ID'])

s = Student('Jan','Kot',23,5435)
print(f"wiek studenta: {s[2]}")
print(f"imię studenta: {s.imie}")
print(f"nazwisko studenta: {getattr(s,'nazwisko')}")

stl = ['Anna','Nowak',21,75646]
sttl = Student._make(stl)
print(f"nowa nt: {sttl}")

std = {'imie':'Olaf','nazwisko':'Kos','wiek':24,'ID':876745}
print(f"krotka s jako słownik: {s._asdict()}")
print(f"kolejna nt: {Student(**std)}")

print(s._fields)
print(sttl)
sttl = sttl._replace(nazwisko='Kowal')
print(sttl)
