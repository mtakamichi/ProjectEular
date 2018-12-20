#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 18
Maximum path sum I
'''
from functools import reduce

numtri='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.splitlines()
numtri = list(map(lambda x: x.split(), numtri))

def list_sum(a,b):
    v = [int(x) + int(y) for x, y in zip(a, b)]
    return v

# Dynamic Programming
def shift_sum_max(pred, curr):
    #shift
    pred1 = list(pred) #deep copy
    pred2 = list(pred)
    pred1.append('00')
    pred2.insert(0,'00')
    #sum
    val1 = list_sum(pred1, curr)
    val2 = list_sum(pred2, curr)
    #max
    valm = [max(x, y) for x, y in zip(val1, val2)]
    return valm

# Main
print(max(reduce(shift_sum_max, numtri)))
