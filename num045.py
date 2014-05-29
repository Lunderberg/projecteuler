#!/usr/bin/env python

from math import sqrt
from itertools import count

def ispentagonal(n):
    val = (1.0+sqrt(1.0+24.0*n))/6.0
    return val==int(val)

def istriangular(n):
    val = (sqrt(1.0+8.0*n)-1.0)/2.0
    return val==int(val)

def ishexagonal(n):
    val = (1.0 + sqrt(1.0+8.0*n))/4.0
    return val==int(val)

def allhexagonal():
    for n in count(1):
        yield n*(2*n-1)

for t in (h for h in allhexagonal() if istriangular(h) and ispentagonal(h)):
    print t
