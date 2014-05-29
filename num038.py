#!/usr/bin/env python

def isPandigital(n):
    t = set(str(n))
    return (n>1e8 and n<1e9 and
            len(t)==9 and ('0' not in t))

def conProduct(val,n):
    return int(''.join(str(val*i) for i in range(1,n+1)))

def prop(val,n):
    return isPandigital(conProduct(val,n))

for i in xrange(1,int(1e9)/3):
    prod = 0
    n = 2
    while prod<1e9:
        prod = conProduct(i,n)
        if isPandigital(prod):
            print prod
        n += 1
