#!/usr/bin/env python

from datetime import datetime,timedelta

def daterange(start,end):
    current = start
    while current<end:
        yield current
        current += timedelta(days=1)

cumsum = 0
for i in daterange(datetime(year=1901,month=1,day=1),
                   datetime(year=2001,month=1,day=1)):
    if i.weekday()==6 and i.day==1:
        cumsum += 1
print cumsum
