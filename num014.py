#!/usr/bin/env python

class CollatzLength(object):
    def __init__(self):
        self.known = {1:1}
    def collatzlength(self,val):
        path = []
        currVal = val
        while currVal not in self.known:
            path.append(currVal)
            if currVal%2==0:
                currVal = currVal/2
            else:
                currVal = 3*currVal+1
        for i,num in enumerate(reversed(path)):
            self.known[num] = self.known[currVal]+i+1
        return self.known[val]
        

cl = CollatzLength()
longest = 0
longeststarter = None
for i in range(1,int(1e6)):
    if cl.collatzlength(i)>longest:
        longest = cl.collatzlength(i)
        longeststarter = i
print longest,longeststarter
