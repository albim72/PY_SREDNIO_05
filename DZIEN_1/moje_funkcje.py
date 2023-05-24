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


