#!/usr/bin/env python

from primes import PrimeFinder

pf = PrimeFinder()

def isPandigital(n):
    t = str(n)
    return all(str(s) in t for s in range(1,len(t)+1))

for p in pf.allprimes():
    if p>1e9:
        break
    if isPandigital(p):
        print p
