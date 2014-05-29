#!/usr/bin/env python

from itertools import cycle,izip,product
import sys

def encrypt(plaintext,key):
    return ','.join(str(ord(v)^ord(k)) for v,k in izip(plaintext,cycle(key)))
def decrypt(cipher,key):
    return ''.join(chr(int(v)^ord(k)) for v,k in izip(cipher.split(','),cycle(key)))

cipher = open('num059_cipher.txt').read().strip()
english = set(open('words.txt').read().split())

def figure_of_merit(plaintext):
    correct = sum(len(word) for word in plaintext.split() if word in english)
    return float(correct)/len(plaintext)

best = ''
bestfom = 0
for i,key in enumerate(product('abcdefghijklmnopqrstuvwxyz',repeat=3)):
    plaintext = decrypt(cipher,key)
    if figure_of_merit(plaintext)>bestfom:
        best = plaintext
        bestfom = figure_of_merit(plaintext)

print sum(ord(s) for s in best)
    
