#!/usr/bin/env python

from primes import PrimeFinder

pf = PrimeFinder()

def step(val):
    return sum(f for f in pf.divisors(val)[:-1])
def isamicable(val):
    middle = step(val)
    final = step(middle)
    return val==final and middle!=val

print sum(i for i in range(2,10001) if isamicable(i))
