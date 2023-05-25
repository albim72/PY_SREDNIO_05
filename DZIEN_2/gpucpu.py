from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer

def normalfunc(a):
    for i in range(10_000_000):
        a[i] += 1

@jit(target_backend='cuda')
def gpufunc(a):
    for i in range(10_000_000):
        a[i] += 1

if __name__ == '__main__':
    n = 10_000_000
    a = np.ones(n,dtype=np.float64)

    start = timer()
    normalfunc(a)
    print(f"funkcja CPU-> czas wykoania {timer()-start} s")

    start = timer()
    gpufunc(a)
    print(f"funkcja GPU-> czas wykoania {timer() - start} s")
