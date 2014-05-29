#!/usr/bin/env python

def diagonals(n):
    yield 1
    cumsum = 1
    for skips in range(2,n+1,2):
        for i in range(4):
            cumsum += skips
            yield cumsum

print sum(diagonals(1001))
