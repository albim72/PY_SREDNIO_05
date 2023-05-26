def liczby():
    for i in range(11):
        yield i*2
p = liczby()
print(p)

for p in liczby():
    print(p)


print("_"*40)

def wznowienie(n,k):
    print("wstrzymanie działania")
    yield 1008
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n+k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n-k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n*k
    print("wznowienie działania")

for i in wznowienie(8,3):
    if i == 1008:
        continue
    print(f"zwrócono wartość: {i}")

print("_"*40)

def complexgen():
    x = 0
    while True:
        print("x-print1")
        y = yield x
        print(type(x))
        print(type(y))
        print("x-print2")
        # x = x + 1
        #warunek if pozwala na wprowadzenie dowolnej wartości x poprzez funkcję send() i kontynuację wyliczania od tej wartości
        if y is None:
            x = x+1
        else:
            x=y

g = complexgen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(g.send(121))
print(next(g))
print(next(g))
print(next(g))


