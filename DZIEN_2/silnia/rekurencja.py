def silnia_rek(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)
