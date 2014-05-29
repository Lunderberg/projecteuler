#!/usr/bin/env python

from fractions import Fraction, gcd
from itertools import count

#Did a few terms, then looked up on OEIS.
#f(n) == Stern(n+1)

def memoize(func):
    known = {}
    def inner(n):
        try:
            return known[n]
        except KeyError:
            res = func(n)
            known[n] = res
            return res
    return inner

@memoize
def Stern(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n%2==0:
        return Stern(n/2)
    else:
        return Stern(n/2)+Stern(n/2+1)

#This iterates over all fractions a_n/a_{n-1}
#The formula is for a_n/a_{n+1}, which is why I return 1/x
def ratl():
    x = Fraction(1,1)
    for i in count():
        yield 1/x
        x = 1/(2*int(x)+1-x)

def f(n):
    return Stern(n+1)

def pos(b,a):
    div = gcd(a,b)
    a /= div
    b /= div
    output = []
    while a>1 or b>1:
        if a<b:
            output.append(b/a)
            b %= a
        else:
            output.append(a/b)
            a %= b
    if len(output)%2==0:
        output[-1] -= 1
        output.append(1)
    return ','.join(str(s) for s in reversed(output))

print '#169:',f(int(10**25))
print '#175:',pos(13,17)
print '#175:',pos(123456789,987654321)
