#!/usr/bin/env python

import primes
import sys
from collections import defaultdict,Counter

n = int(sys.argv[1])

pf = primes.PrimeFinder()
factors = defaultdict(int)
for i in range(1,n+1):
    for prime,count in Counter(pf.primefactors(i)).items():
        factors[prime] = max(factors[prime],count)

output = 1
for prime,count in factors.items():
    output *= prime**count
print output
