#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 19
How many Sundays fell on the first of the month during the twentieth century?
'''
from itertools import accumulate, chain

common_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def year2days(y):
    if (y%4 == 0 and y%100 != 0) or y%400 == 0:
        return leap_days
    else:
        return common_days

days = map(year2days, range(1900,2001))
days = list(chain.from_iterable(days)) #flatten
days.insert(0, 1) # 1st Jan 1900 is Monday
days.pop(-1) # delete Jan 2001
mc_days = list(map(lambda x: x%7, accumulate(days)))
del mc_days[0:12] # delete the year 2000
print(sum(1 for i in mc_days if i== 0)) #count Sundays
