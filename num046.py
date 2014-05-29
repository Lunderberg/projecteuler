#!/usr/bin/env python

from itertools import count
from primes import PrimeFinder
from math import sqrt

pf = PrimeFinder()

def tocheck():
    for i in count(3,2):
        if not pf.isprime(i):
            yield i

def testval(val):
    for p in pf.primesunder(val):
        test = sqrt((val-p)/2.0)
        if test==int(test):
            return True
    else:
        return False

for i in tocheck():
    if not testval(i):
        print i
        break
