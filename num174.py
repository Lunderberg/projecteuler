#!/usr/bin/env python

from math import sqrt
from collections import defaultdict

maxtiles = 1000000
#maxtiles = 100

def biggestside(tiles):
    return (tiles+1)/2
def holesizes(tiles,side):
    try:
        hole = int(sqrt(side*side - tiles))
        hole = hole if hole else 1
    except ValueError:
        hole = 1
    hole += (side-hole)%2
    while hole<side:
        yield hole
        hole += 2
def tiles(side,hole):
    return side*side - hole*hole

combos = defaultdict(int)

for side in xrange(biggestside(maxtiles)+1):
    #for hole in xrange(smallesthole(maxtiles,side),biggesthole(side)+2,2):
    for hole in holesizes(maxtiles,side):
        combos[tiles(side,hole)] += 1

def N(n):
    return sum(1 for i,val in combos.items() if i<=maxtiles and val==n)

print '#173:',sum(val for i,val in combos.items() if i<=maxtiles)
print '#174:',sum(N(i) for i in range(1,11))
