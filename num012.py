#!/usr/bin/env python

from primes import PrimeFinder

def triangular():
    cumsum = 0
    i = 1
    while True:
        cumsum += i
        i += 1
        yield cumsum

pf = PrimeFinder()

for tri in triangular():
    numdivisors = len(pf.divisors(tri))
    if numdivisors>500:
        print tri
        break
