from abc import ABCMeta, abstractmethod

class IPojazd(metaclass=ABCMeta):
    @abstractmethod
    def spal_100(self,odl,litry):
        raise NotImplementedError(f"obowiązkowo zaimplementuj metodę spal_100()")
    
    @abstractmethod
    def kosztyprzejazdu(self,odl,litry,cena_l):
        raise NotImplementedError(f"obowiązkowo zaimplementuj metodę kosztyprzejazdu()")
