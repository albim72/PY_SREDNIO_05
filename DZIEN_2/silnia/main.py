from fsilnia import silnia
import sys


try:
    sys.set_int_max_str_digits(0x1000000)
    print("obliczenie silnii!")
    n = int(input("podaj wartość n: "))
    print(f"silnia z {n} wynosi: {silnia(n)}.")
except ValueError as er:
    print(er)
