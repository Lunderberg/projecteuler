#!/usr/bin/env python

def hasprop(val):
    base10 = str(val)
    base2 = format(val,'b')
    return base10==base10[::-1] and base2==base2[::-1]

print sum(i for i in range(1,int(1e6)) if hasprop(i))
