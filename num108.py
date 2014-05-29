#!/usr/bin/env python

from primes import PrimeFinder, product
from itertools import count,izip
from math import log

pf = PrimeFinder()

def spread(n,previous=-1):
    previous = previous if previous!=-1 else n
    if n==0:
        yield tuple()
    else:
        for first in range(min(n,previous),0,-1):
            for rest in spread(n-first,first):
                yield (first,)+rest

def numSolutions(n):
    return sum(1 for x in xrange(n+1,2*n+1) if n*x%(x-n)==0)
def numSolutionsFastest(n):
    return pf.numdivisors(n*n)/2+1


def firstAbove(val):
    found = None
    maxFactorsNeeded = None
    for numFactors in count(1):
        if maxFactorsNeeded is not None and numFactors > maxFactorsNeeded: #Found one solution and checked as high as needed.
            break
        for factorCount in spread(numFactors):
            num = product(prime**val for prime,val in izip(pf.allprimes(),factorCount))
            if found is not None and num>found: #Found a solution, and this number is too high.
                continue
            sols = numSolutionsFastest(num)
            if sols>val:
                if found is None or num<found: #New solution is the best.
                    found = num
                    maxFactorsNeeded = log(found,2)
    return found

print firstAbove(1000)
print firstAbove(4000000)
