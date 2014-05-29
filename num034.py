#!/usr/bin/env python

from math import factorial

def hasprop(val):
    return sum(factorial(int(s)) for s in str(val))==val

#Assume an n-digit number.
#The sum of factorials can be at most 9!*n.
#Therefore, must check up to all 7-digit numbers.
for i in range(3,int(1e7)):
    if i%1000000==0:
        print "Checking",i
    if hasprop(i):
        print i
