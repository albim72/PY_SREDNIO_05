from dataclasses import dataclass,field

@dataclass
class Osoba:
    id:int
    imie:str
    nazwisko:str
    wiek:int
    miasto: str

    def __repr__(self):
        return f"osoba {self.imie} {self.nazwisko}, wiek: {self.wiek} -> miasto {self.miasto}"


os1 = Osoba(6,"Jan","Kos",45,"Tarnów")
print(os1)
print(os1.imie)

@dataclass(init=False)
class Pracownik(Osoba):
    firma:str
    latapracy:int
    stanowisko:str
    wynagrodzenie:float
    #full_name: str = field(init=False, repr=False)

    def __init__(self,id,imie,nazwisko,wiek,latapracy,stanowisko,wynagrodzenie=3700):
        super().__init__(id,imie,nazwisko,wiek,"Kraków")
        self.latapracy = latapracy
        self.stanowisko = stanowisko
        self.wynagrodzenie = wynagrodzenie
        self.firma = "ABC Sp zoo"
        self.full_name: str = field(init=True, repr=False)

    def __post_init__(self):
        self.full_name = self.imie + " " + self.nazwisko

    def printpracownik(self):
        return f"Pracownik {self.imie} {self.nazwisko}, stanowisko: {self.stanowisko} -> " \
               f"wynagrodzenie: {self.wynagrodzenie} zł"

pr1 = Pracownik(8,"Anna","Kot",36,6,"księgowa",5200)
print(pr1)
print(pr1.printpracownik())
print(type(os1))
print(type(pr1))

print(pr1.full_name)



