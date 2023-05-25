from abc import ABC, abstractmethod

class Abstrakcyjna(ABC):
    def __init__(self,funkcja,x,y,*args):
        self.x=x
        self.y=y
        funkcja(*args)

    def msg(self):
        return f"dane -> x = {self.x}, y = {self.y}."

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_xy(self):
        return self.x*3+self.y*2


def opis(id,msg):
    print(f"wiadomość nr {id} -> {msg}")


class Regularna(Abstrakcyjna):

    def policz(self):
        return self.x,self.y,self.x*2

    def policz_xy(self):
        return super().policz_xy() + 25


rg = Regularna(opis,4,8,12,"informacja 34234")
xs,ys,zs = rg.policz()
print(f"wynik 1 = x-> {xs}, y -> {ys}, dwukrtoność x: {zs}")
print(f"wynik 2 = {rg.policz_xy()}")
