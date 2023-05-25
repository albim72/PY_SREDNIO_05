class Kolor:
    def __init__(self,nazwak,oznaczenie):
        self.nazwa_koloru = nazwak
        self.oznaczenie = oznaczenie

    def __repr__(self):
        return f"Kolor {self.nazwa_koloru}, oznaczenie {self.oznaczenie}."

class Format:
    def __init__(self,nazwaf,rodzaj):
        self.nazwa_formatu = nazwaf
        self.rodzaj = rodzaj

    def __repr__(self):
        return f"Format {self.nazwa_formatu}, oznaczenie {self.rodzaj}."


# k = Kolor("czarny",34534)
# print(k)
# k = k.__init__("czerwony",754456)
# k = k.__repr__()
# print(k)

class Paleta(Kolor,Format):
    def __init__(self, nazwak, oznaczenie, nazwaf,rodzaj, id):
        Kolor.__init__(self,nazwak, oznaczenie)
        Format.__init__(self,nazwaf, rodzaj)
        self.id = id

    # def __str__(self):
    #     return "nowa paleta!"
    
    def __repr__(self):
        return f"Paleta -> id: {self.id}, " \
               f"Kolor {self.nazwa_koloru}, oznaczenie {self.oznaczenie}. " \
               f"Format {self.nazwa_formatu}, oznaczenie {self.rodzaj}."



p = Paleta("czarny",5446,"dwg","tekstury","CP535")
print(p)


