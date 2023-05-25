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
