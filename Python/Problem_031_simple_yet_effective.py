#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 31
How many different ways can £2 be made using any number of coins?
'''
import time
start=time.time()
limit = 200 + 1
pat = ([True
        for a in range(0, limit, 100)
        for b in range(0, limit-a, 50)
        for c in range(0, limit-(a+b), 20)
        for d in range(0, limit-(a+b+c), 10)
        for e in range(0, limit-(a+b+c+d), 5)
        for f in range(0, limit-(a+b+c+d+e), 2)])
print(len(pat)+1)
print(time.time()-start)
