#!/usr/bin/env python

from primes import PrimeFinder

pf = PrimeFinder()

upperlimit = 1000000

primes = list(pf.primesunder(upperlimit))

maxlength = 1
bestprime = None
for startpos in xrange(len(primes)-1):
    for endpos in xrange(startpos+maxlength,len(primes)):
        currSum = sum(primes[startpos:endpos])
        if currSum in primes and endpos-startpos>maxlength:
            maxlength = endpos-startpos
            bestprime = sum(primes[startpos:endpos])
            print startpos,endpos,maxlength,bestprime
        elif currSum>upperlimit:
            break
print 'Done',bestprime,maxlength
