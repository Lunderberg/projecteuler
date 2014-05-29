#!/usr/bin/env python

from math import factorial

def choose(n,m):
    return factorial(n)/factorial(m)/factorial(n-m)

print choose(40,20)
