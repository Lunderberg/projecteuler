#!/usr/bin/env python

from math import sqrt
from itertools import chain, combinations
import operator
from collections import Counter

def product(inputList,initial=1):
    return reduce(operator.mul,inputList,initial)

class PrimeFinder(object):
    def __init__(self):
        """
        Initializes the list of all currently known prime numbers.
        Also tracks the maximum checked value.
        """
        self.primes = [2]
        self.maxchecked = 2
    def isprime(self,val):
        """
        Returns whether a given value is prime.
        Checks whether each number up to that given number is prime,
          then checks whether the given number is in the list of known primes.
        """
        while self.maxchecked<=val:
            self.checknext()
        return val in self.primes
    def advanceto(self,val):
        while self.maxchecked<=val:
            self.checknext()
    def allprimes(self):
        """
        An iterator returning all prime numbers, one at a time.
        First, returns all the known values.
        Then, continues searching for more prime numbers.
        """
        #For more information on this technique, look up iterators.
        for prime in self.primes:
            yield prime
        while True:
            yield self.findnextprime()
    def primesunder(self,val):
        for prime in self.allprimes():
            if prime<val:
                yield prime
            else:
                break
    def findnextprime(self):
        """
        Searches for the next prime number.
        When found, returns that new prime number.
        """
        while not self.checknext():
            pass
        return self.primes[-1]
    def checknext(self):
        """
        Checks the next number to see if it is prime.
        A number n is prime if it is not divisible by any prime number between 2 and sqrt(n)
        """
        val = self.maxchecked+1
        maxChecking = int(sqrt(val))
        isprime = True
        for prime in self.primes:
            if val % prime == 0:
                isprime = False
                break
            elif prime>maxChecking:
                break
        if isprime:
            self.primes.append(val)
        self.maxchecked = val
        return isprime
    def primefactors(self,val):
        """
        Finds the prime factors of a given number.
        Starts at the lowest prime number, searching for divisors.
        """
        if val<1:
            raise ValueError('Illogical to find prime factors of non-natural number')
        factors = []
        remainder = val
        for prime in self.allprimes():
            while remainder % prime == 0:
                factors.append(prime)
                remainder /= prime
            if remainder==1:
                break
        return factors
    def divisors(self,val):
        """
        Returns a list of all divisors of the requested value.
        First, makes a list of all prime factors, then makes all products of these factors.
        """
        factors = self.primefactors(val)
        allsubsets = chain(*[combinations(factors,n) for n in range(len(factors)+1)])
        output = []
        for subset in allsubsets:
            output.append(product(subset))
        return sorted(list(set(output)))
    def numdivisors(self,val):
        factors = self.primefactors(val)
        return product(num+1 for num in Counter(factors).values())
        
        

if __name__=='__main__':
    pf = PrimeFinder()
    print pf.advanceto(int(1e6))
