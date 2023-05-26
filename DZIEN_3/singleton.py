class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=Singleton):
    pass

class RegularClass():
    pass

r1 = RegularClass()
r2 = RegularClass()

print(r1,r2)
print(r1==r2)

s1 = SingletonClass()
s2 = SingletonClass()
print(s1,s2)
print(s1==s2)
