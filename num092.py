#!/usr/bin/env python

ends = {1:1,89:89}

def checkval(n):
    path = []
    while n not in ends:
        path.append(n)
        n = sum(int(s)*int(s) for s in str(n))
    final = ends[n]
    for val in path:
        ends[val] = final
    return final

for i in range(1,int(1e7)):
    if i%100000==0:
        print 'Checking',i
    checkval(i)
print sum(1 for val in ends.values() if val==89)
