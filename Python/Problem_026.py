#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 26
Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part.
'''

def len_cycle(n):
    nines=9
    for i in range(1,10000):
        if(nines % n == 0):
            return i
        nines=int('9'+str(nines))

nl =  [x for x in range(3,1000) if x%2!=0 and x%5!=0]
lcl = list(map(len_cycle, nl))
print(lcl[lcl.index(max(lcl))])
