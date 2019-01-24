#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 38
What is the largest 1 to 9 pandigital 9-digit number that can be 
formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
pl = []
for i in range(1, 9999):
    ns = str(i)
    for j in range(2, 10):
        ns += str(j*i)
        if len(ns) > 9:
            break
        if len(set(ns)-{'0'}) == 9:
            pl.append(int(''.join(list(ns))))
            
print(pl[-1])