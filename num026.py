#!/usr/bin/env python

from itertools import count

def repeats(n):
    known = {}
    for i in count(1):
        remainder = (10**i) % n
        if remainder==0:
            return 0
        elif remainder in known:
            return i - known[remainder]
        else:
            known[remainder] = i

print max(range(1,1001),key=repeats)
