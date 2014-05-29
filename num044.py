#!/usr/bin/env python

from math import sqrt
from itertools import count

def ispentagonal(n):
    val = (1.0+sqrt(1.0+24.0*n))/6.0
    return val==int(val)

def allpentagonal():
    for n in count(1):
        yield n*(3*n-1)/2

def pentagonalunder(n):
    for p in allpentagonal():
        if p<n:
            yield p
        else:
            break

for p in pentagonalunder(1e8):
    for u in pentagonalunder(p):
        if ispentagonal(p+u) and ispentagonal(p-u):
            print p,u,p-u
