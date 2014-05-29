#!/usr/bin/env python

from collections import Counter

values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
          'T':10,'J':11,'Q':12,'K':13,'A':14}
hands = []
for line in open('num054_poker.txt'):
    line = line.split()
    if not line:
        continue
    line = [(values[i],j) for i,j in line]
    hands.append((line[:5],line[5:]))

def strength(hand):
    is_flush = all(hand[0][1]==c[1] for c in hand[1:])
    values = tuple(sorted((i for i,j in hand),reverse=True))
    is_straight = any(set(values)==set(range(i,i+5)) for i in range(2,10))
    c = Counter(values)
    high_card = max(values)
    singles = [v for v,a in c.items() if a==1]
    doubles = [v for v,a in c.items() if a==2]
    triples = [v for v,a in c.items() if a==3]
    quadruples = [v for v,a in c.items() if a==4]
    
    if (is_flush and is_straight and high_card==14):
        return (10,)
    elif (is_flush and is_straight):
        return (9,high_card(hand))
    elif quadruples:
        return (8,quadruples[0])
    elif triples and doubles:
        return (7,triples[0])
    elif is_flush:
        return (6,) + values
    elif is_straight:
        return (5,high_card)
    elif triples:
        return (4,triples[0],max(singles),min(singles))
    elif len(doubles)==2:
        return (3,max(doubles),min(doubles),singles[0])
    elif doubles:
        return (2,doubles[0],) + tuple(sorted(singles,reverse=True))
    else:
        return (1,) + values

print sum(1 for hand1,hand2 in hands if strength(hand1)>strength(hand2))
