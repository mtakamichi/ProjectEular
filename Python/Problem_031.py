#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 31
How many different ways can £2 be made using any number of coins?
'''
#import time
from functools import lru_cache
coins = [200, 100, 50, 20, 10, 5, 2, 1]
#start=time.time()
@lru_cache(maxsize=1000000)
def combi_of_coins(total, max_cp):
    if total == 0:
        return 1 #残額0で終了
    combi = 0
    #探索範囲はcoinsリストを使用可能最大コインで制約したもの
    for cp in list(filter(lambda x: x <= max_cp, coins)):
        if total-cp >= 0:
            if cp == 1:
                #使用可能最大コインが1になったら探索打ち切り
                combi += combi_of_coins(0, 1)
            else:
                #残額と使用可能最大コインを更新
                combi += combi_of_coins(total-cp, cp)
    return combi

#combi_of_coins(a,b)は残額a，これまでの使用可能最大コインbでの組合せ数を返す
print(combi_of_coins(200, 200))
#print(time.time()-start)
