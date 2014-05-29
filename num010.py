#!/usr/bin/env python

import primes

pf = primes.PrimeFinder()
pf.advanceto(int(2e6))
print sum(pf.primes)
