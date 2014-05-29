#!/usr/bin/env python

from math import factorial
from primes import product
from collections import Counter

def multifactorial(*args):
    return factorial(sum(args))/product(factorial(a) for a in args)
def choose(n,m):
    return multifactorial(n-m,m)

def spread(n,maxallowed=-1):
    maxallowed = maxallowed if maxallowed!=-1 else n
    if n==0:
        yield tuple()
    else:
        for first in range(min(n,maxallowed),0,-1):
            for rest in spread(n-first,first):
                yield (first,)+rest
def combos(n,maxallowed=-1):
    for s in spread(n,maxallowed):
        if len(s)<=10:
            yield s
def digitchoice(c):
    return factorial(10)/product(factorial(v) for v in Counter(c).values())/factorial(10-len(c))

cumsum = 0
for c in combos(18,3):
    print c
    digitorder = multifactorial(*c)
    cumsum += digitchoice(c)*digitorder
cumsum = cumsum*9/10
print '\n',cumsum, len(str(cumsum))
    
