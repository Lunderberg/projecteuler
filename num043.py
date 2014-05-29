#!/usr/bin/env python

from itertools import permutations

def pandigitals():
    for t in permutations('0123456789'):
        if t[0]!='0':
            yield ''.join(t)

def hasprop():
    for val in pandigitals():
        if (int(val[1:4])%2==0 and
            int(val[2:5])%3==0 and
            int(val[3:6])%5==0 and
            int(val[4:7])%7==0 and
            int(val[5:8])%11==0 and
            int(val[6:9])%13==0 and
            int(val[7:10])%17==0):
            yield int(val)

print sum(hasprop())
