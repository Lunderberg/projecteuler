#!/usr/bin/env python

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

text = open('num022_names.txt').read()
names = [s[1:-1] for s in text.split(',')]
names.sort()

cumsum = 0
for i,name in enumerate(names):
    letterscore = sum(alphabet.index(l)+1 for l in name)
    cumsum += (i+1)*letterscore
print cumsum
