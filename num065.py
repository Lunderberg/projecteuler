#!/usr/bin/env python

from fractions import Fraction
from primes import product

def continuedFraction(vals):
    if len(vals)==1:
        return Fraction(vals[0],1)
    else:
        currVal = Fraction(vals[-1],1)
        for denom in reversed(vals[:-1]):
            currVal = denom + 1/currVal
        return currVal

def eseq(n):
    output = [2]
    for k in range(n/3 + 1):
        output.extend([1,2*(k+1),1])
    return output[:n]

for i in range(1,11):
    print eseq(i)
    print continuedFraction(eseq(i))

print sum(int(s) for s in str(continuedFraction(eseq(100)).numerator))
