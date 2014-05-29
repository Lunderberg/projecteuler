#!/usr/bin/env python

from fractions import Fraction

def continuedFraction(vals):
    if len(vals)==1:
        return Fraction(vals[0],1)
    else:
        currVal = Fraction(vals[-1],1)
        for denom in reversed(vals[:-1]):
            currVal = denom + 1/currVal
        return currVal

def expansion(n):
    return continuedFraction([1]+[2]*n)

cumsum = 0
for n in range(1,1001):
    print n
    f = expansion(n)
    if len(str(f.numerator))>len(str(f.denominator)):
        cumsum += 1
print cumsum
