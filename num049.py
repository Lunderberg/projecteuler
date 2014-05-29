#!/usr/bin/env python

from primes import PrimeFinder
from itertools import permutations, combinations

pf = PrimeFinder()

def numberperm(val):
    for perm in permutations(str(val)):
        yield int(''.join(perm))

def primepermutations(val):
    return sorted(list(set(perm for perm in numberperm(val) if pf.isprime(perm))))

def increasingsequences(val,n):
    return set(combinations(primepermutations(val),n))

def hasproperty(val):
    if not pf.isprime(val):
        return False
    for seq in increasingsequences(val,3):
        if (seq[0]==val) and seq[1]-seq[0]==seq[2]-seq[1]:
            return seq
    else:
        return False
    
for i in range(1000,10000):
    if hasproperty(i):
        print hasproperty(i)
