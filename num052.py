#!/usr/bin/env python

from itertools import count

def hasprop(n):
    if str(n)[0]!='1':
        return False
    reference = sorted(list(str(n)))
    return all(reference==sorted(list(str(n*mult))) for mult in range(2,7))

for n in count():
    if n%100000==0:
        print 'Checking',n
    if hasprop(n):
        print n
        break
