#!/usr/bin/env python

from itertools import count

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def triangular():
    cumsum = 0
    for i in count(1):
        cumsum += i
        yield cumsum

def score(word):
    return sum(alphabet.index(s)+1 for s in word)
def istriangular(num):
    for tri in triangular():
        if num==tri:
            return True
        elif tri>num:
            return False

words = [word[1:-1] for word in open('num042_words.txt').read().split(',')]

print sum(1 for word in words if istriangular(score(word)))
