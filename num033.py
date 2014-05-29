#!/usr/bin/env python

from fractions import Fraction
from primes import product

def isDigitCancelling(a,b):
    if a==b:
        return False
    elif (a%10==0) and (b%10==0):
        return False
    orig = Fraction(a,b)
    if a/10==b/10 and a%10 and b%10 and Fraction(a%10,b%10)==orig:
        return True
    elif a/10==b%10 and a%10 and Fraction(a%10,b/10)==orig:
        return True
    elif a%10==b/10 and b%10 and Fraction(a/10,b%10)==orig:
        return True
    elif a%10==b%10 and Fraction(a/10,b/10)==orig:
        return True
    else:
        return False

print [(a,b) for a in range(10,100) for b in range(a,100) if isDigitCancelling(a,b)]
print product(Fraction(a,b) for a in range(10,100) for b in range(a,100) if isDigitCancelling(a,b))
