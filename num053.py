#!/usr/bin/env python

from math import factorial

def choose(n,m):
    return factorial(n)/factorial(m)/factorial(n-m)

found = 0
for n in range(1,101):
    for m in range(0,n+1):
        if choose(n,m)>1000000:
            found += 1
print found
