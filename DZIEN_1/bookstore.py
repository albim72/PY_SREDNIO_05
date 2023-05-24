class Book:
    def __init__(self,id,tytul,autor,cena=30):
        self.idksiazki = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    def __repr__(self):
        return f"książka: {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, " \
               f"oprawa: {self.oprawa}"

    def create_book(self):
        print("nowa książka została utworzona...")

    def rabat(self,proc):
        return proc*self.cena/100


b1 = Book(34,"Wiedźmin","Andrzej Sapkowski",42)
print(f"rabat: {b1.rabat(12)} zł")
print(b1)
print("____________________________________")

b2 = Book(37,"Hobbit","J.R.R. Tolkien",39)
print(f"rabat: {b1.rabat(9)} zł")
print(b2)

