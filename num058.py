#!/usr/bin/env python

from itertools import count
from primes import PrimeFinder
pf = PrimeFinder()

def isint(x):
    return int(x)==x

def diagonals():
    yield 1
    cumsum = 1
    for skips in count(2,2):
        for i in range(4):
            cumsum += skips
            yield cumsum

def allcorners():
    d = diagonals()
    yield (1,)
    while True:
        yield (next(d),next(d),next(d),next(d))

side = -1
primes = 0
vals = 0
for corners in allcorners():
    side += 2
    vals += len(corners)
    primes += sum(1 for c in corners if pf.isprime(c))
    if 10*primes<vals and side>1:
        print side
        break
    if not (side-1)%100:
        print 'Checking: {0} ({1:.1f}%)'.format(side,100*float(primes)/vals)
