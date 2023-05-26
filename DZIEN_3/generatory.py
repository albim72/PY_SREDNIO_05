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
    print(f"zwrócono wartość: {i}")

