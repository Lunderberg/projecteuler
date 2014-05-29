#!/usr/bin/env python

from itertools import permutations

def pandigital():
    for perm in permutations('123456789'):
        for i in range(1,8):
            for j in range(i+1,9):
                a = int(''.join(perm[:i]))
                b = int(''.join(perm[i:j]))
                c = int(''.join(perm[j:]))
                if a*b==c:
                    yield a,b,c

print sum(set(c for a,b,c in pandigital()))
