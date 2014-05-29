#!/usr/bin/env python

from primes import PrimeFinder

pf = PrimeFinder()

def isabundant(n):
    return sum(pf.divisors(n)[:-1])>n
abun = [n for n in range(1,28124) if isabundant(n)]

remainder = set(range(1,28124))
for a in abun:
    for b in abun:
        remainder -= set([a+b])
print sum(remainder)
