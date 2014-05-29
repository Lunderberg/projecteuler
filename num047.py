#!/usr/bin/env python

from primes import PrimeFinder
from itertools import count

pf = PrimeFinder()

def memoize(func):
    known = {}
    def inner(n):
        try:
            return known[n]
        except KeyError:
            res = func(n)
            known[n] = res
            return res
    return inner

@memoize
def numfactors(n):
    return len(set(pf.primefactors(n)))

searching = 4
for i in count(2):
    if all(numfactors(t)>=searching for t in range(i,i+searching)):
        print i
        break
