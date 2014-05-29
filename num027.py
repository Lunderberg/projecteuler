#!/usr/bin/env python

from primes import PrimeFinder
from itertools import count

pf = PrimeFinder()

def primelength(vals):
    a,b = vals
    length = 0
    for n in count():
        num = n*n + a*n + b
        if num>1 and pf.isprime(num):
            length += 1
        else:
            break
    return length

print max(((a,b)
           for a in range(-1000,1000) for b in range(-1000,1000)),
          key = primelength)
