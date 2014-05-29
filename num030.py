#!/usr/bin/env python

def hasprop(n,power):
    return n==sum(pow(int(s),power) for s in str(n))
def maxtocheck(power):
    digits = 1
    while digits*(9**power) > 10**digits:
        digits += 1
    return 10**digits

power = 5
cumsum = 0
for i in range(2,maxtocheck(power)):
    if hasprop(i,power):
        print i
        cumsum += i
print 'Total:',cumsum
