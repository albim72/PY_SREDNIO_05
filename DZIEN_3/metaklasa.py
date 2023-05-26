#dziedziczenie klasy type czyni z klasy metaklasę
class MojaMeta(type):
    def __new__(cls, clasname, bases, attribsdict):
        print(f"nazwa klasy: {clasname}")
        print(f"dziedziczone klasy: {bases}")
        print(f"słownik atrybutów: {attribsdict}")
        return type.__new__(cls, clasname, bases, attribsdict)


class Zwykla:
    pass

class Base(Zwykla,metaclass=MojaMeta):
    pass

class Nastepna(Base):
    pass

class E:
    pass

class Ostatnia(E,Nastepna):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c = 100

    def info(self):
        return "informacja"

    @property
    def msg(self):
        return "wiadomość"

    kolor = "czarny"


ost = Ostatnia(4,6)
print(ost.info())
print(ost.msg)


