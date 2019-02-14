#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
'''

nml_to_let={1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',\
8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', \
14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',\
19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',\
70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'onethousand', 'and':'and' }

def num_to_nml(x):
    y=[]
    if x == 1000:
        y.append(1000)
        x -= 1000
    elif x//100 > 0:
        y.append(x//100)
        y.append(100)
        x  -= x//100*100
        if x!=0:
            y.append('and')
    if x//10>1:
        y.append(x//10*10)
        x -= x//10*10
    elif x//10==1:
        y.append(x)
        x -= x
    if x!=0:
        y.append(x)
    y2 = ''.join(list(map(lambda x: nml_to_let[x], y)))
    return len(y2)

print(sum(list(map(num_to_nml, range(1,1001)))))
