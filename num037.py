#!/usr/bin/env python

from primes import PrimeFinder
from math import log

pf = PrimeFinder()

def isTruncatable(p):
    if not pf.isprime(p) or p<10:
        return False
    copy = p
    while copy>0:
        if not pf.isprime(copy):
            return False
        copy /= 10
    copy = p
    while copy>0:
        if not pf.isprime(copy):
            return False
        copy %= 10**int(log(copy,10))
    return True

found = []
printed = 0
delta = int(1e5)
for p in pf.allprimes():
    if p>printed+delta:
        printed += delta
        print 'Checking',printed
    if isTruncatable(p):
        found.append(p)
        if len(found)==11:
            break
print sum(found)
