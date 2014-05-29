#!/usr/bin/env python

def ispalindrome(n):
    return str(n)==str(n)[::-1]
def reversednum(n):
    return int(str(n)[::-1])
def islychrel(n):
    for i in range(50):
        n += reversednum(n)
        if ispalindrome(n):
            return False
    return True

for i in range(10001):
    if islychrel(i):
        print i

print sum(1 for i in range(10001) if islychrel(i))
