#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 25
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

pred, curr = 0, 1
ind=1
while(len(str(curr))<1000):
    pred, curr = curr, pred+curr
    ind += 1

print(ind)
