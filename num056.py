#!/usr/bin/env python

def digitalsum(n):
    return sum(int(s) for s in str(n))

print max(digitalsum(a**b) for a in range(1,100) for b in range(1,100))
