#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 25
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

pred=0
curr=1
succ=1
ind=1
while(len(str(succ))<1000):
    succ = pred + curr
    pred = curr
    curr = succ
    ind += 1

print(ind)
