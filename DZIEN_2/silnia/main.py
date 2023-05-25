from fsilnia import silnia
from rekurencja import silnia_rek
import sys
import time


try:
    sys.set_int_max_str_digits(0x1000000)
    sys.setrecursionlimit(0x1000000)
    print("obliczenie silnii!")
    n = int(input("podaj wartość n: "))
    s1 = time.perf_counter()
    print(f"silnia z {n} wynosi: {silnia(n)}.")
    k1 = time.perf_counter()
    dt1 = k1-s1
    s2= time.perf_counter()
    print(f"silnia rekurencyjna z {n} wynosi: {silnia_rek(n)}.")
    k2 = time.perf_counter()
    dt2 = k2-s2

    print(f"czas wykonania:\nsilnia iteracyjna: {dt1} s,\n"
          f"silnia rekurencyjna: {dt2} s")

except ValueError as er:
    print(er)
