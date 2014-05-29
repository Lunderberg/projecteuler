#!/usr/bin/env python

def sols(p):
    for a in range(1,p-2):
        for b in range(a,p-a-1):
            c = p-a-b
            if a*a+b*b==c*c:
                yield a,b,c
def numsols(p):
    return sum(1 for s in sols(p))


print max(range(1,1001),key=numsols)
