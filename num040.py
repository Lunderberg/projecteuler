#!/usr/bin/env python

from itertools import count

def champernowne():
    for i in count():
        for s in str(i):
            yield int(s)

prod = 1
for i,digit in enumerate(champernowne()):
    if i in [1,10,100,1000,10000,100000,1000000]:
        prod *= digit
        if i==1000000:
            break

print prod
