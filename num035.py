#!/usr/bin/env python

from primes import PrimeFinder

pf = PrimeFinder()


def rotations(n):
    strList = list(str(n))
    for i in range(len(strList)):
        yield int(''.join(strList[i:] + strList[:i]))

def iscircularprime(n):
    return all(pf.isprime(rot) for rot in rotations(n))

total = 0
for i in range(2,1000000):
    if i%10000==0:
        print 'checking',i
    if iscircularprime(i):
        total += 1
print total

