#!/usr/bin/env python

conversion = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',
              11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
              16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
              30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

def num2word(val):
    if val >= 1000:
        thousands = "{0} thousand".format(num2word(val/1000))
        smaller = ", {0}".format(num2word(val%1000)) if val%1000 else ""
        return thousands+smaller
    elif val >= 100:
        hundreds = "{0} hundred".format(num2word(val/100))
        smaller = " and {0}".format(num2word(val%100)) if val%100 else ""
        return hundreds+smaller
    elif val in conversion:
        return conversion[val]
    else:
        return "{0}-{1}".format(num2word((val/10)*10),num2word(val%10))

allNums = ' '.join(num2word(i) for i in range(1,1001))
alphas = 'abcdefghijklmnopqrstuvwxyz'
print sum(1 for s in allNums if s in alphas)
