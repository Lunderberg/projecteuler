#!/usr/bin/env python

from primes import PrimeFinder
pf = PrimeFinder()

def allFamilies(n):
    numStr = str(n)
    for s in '0123456789':
        if s in numStr:
            yield numStr.replace(s,'*')

families = {}
def familySize(family):
    if family in families:
        return families[family]
    cumsum = 0
    for s in '123456789':
        num = int(family.replace('*',s))
        if pf.isprime(num):
            cumsum += 1
    if family[0]!='*' and pf.isprime(int(family.replace('*','0'))):
        cumsum += 1
    families[family] = cumsum
    return cumsum

def biggestFamily(n):
    return max(((familySize(family),family) for family in allFamilies(n)),
               key = lambda t:t[0])

import code; code.interact(local=locals())

currentBiggest = (0,'0')
for i,prime in enumerate(PrimeFinder().allprimes()):
    if biggestFamily(prime)>currentBiggest:
        currentBiggest = biggestFamily(prime)
        print currentBiggest,prime
    
