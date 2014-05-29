#!/usr/bin/env python

denominations = [200,100,50,20,10,5,2,1]

def spread(amount,denominations):
    biggest = denominations[0]
    maxbiggest = amount/biggest
    if len(denominations)==1:
        yield [maxbiggest]
    else:
        for first in range(maxbiggest+1):
            for rest in spread(amount - first*biggest,denominations[1:]):
                yield [first] + rest

print sum(1 for s in spread(200,denominations))
