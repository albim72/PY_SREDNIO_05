import math

#przykład 1

def f(x):
    return x**4
n=100
def policz(a,b,c,y):
    global n
    n = (a+b)*y-c + n + f(b)
    return n

print(policz(6,2,5,7))
print(n)

#przykład 2
def gx(n,m=1,k=3,b=5):
    return math.sqrt(n+m)*k-b

print(gx(8,4,1,9))
print(gx(8,4,1))
print(gx(8,4))
print(gx(8))
print(gx(12,b=6))
print(gx(7,b=4,k=2))


#przykład 3
def rank(*lang,nrrank,**kwargs):
    print(f'ranking języków programowania nr {nrrank}, pierwsze miejsce: {lang[0]}, '
          f'drugie miejsce: {lang[1]}, trzecie miejsce: {lang[2]}')
    print(kwargs)

rank("Python","Java","C++",nrrank=23,cos = 3253245)

rank("Python","C#","Java","JavaScript","C++",nrrank=23)


#funkcje anonimowe
#funkcja lambda

print((lambda e:e**3)(4))
print((lambda e:e**3 if e>10 else e-1)(4))
print((lambda e:e**3 if e>10 else e-1)(11))

def cos(e):
    return e**3

print(cos(4))

r = lambda a,b,c:(a+b)*c

print(r(3,7,2))
print(r(4.55,2.2,1))

def multi(k):
    return lambda a:a*(k-1)

d = multi(56)
print(d(9))
print(multi(18)(7))


def druga(k):
    return k + 1

def innemulti(a,k):
    return a*druga(k)

print(innemulti(4,7))

mojalista = [n**8 for n in range(10_000_000) if n%2==0] #list comprehension
print(mojalista)
sl = sum(mojalista)
print(sl)

ekstralista = []
for n in range(10_000_000):
    if n % 2 == 0 and n%10 == 6:
        ekstralista.append(n**8)

print(len(ekstralista))

#zastosowania funkcji

lb = [67,9,12,-4,0,112,9,-99,178,12,-2,14,67,55,111,-3]

