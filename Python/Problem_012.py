
#!/usr/bin/env,python3
#,-*-,coding:,utf-8,-*-
'''
Problem 12
What is the value of the first triangle number to have over five hundred divisors?
'''
n=1
while(True):
    t=int(n*(n+1)/2)
    sqt = int(t**0.5)
    divl = [t%x==0 for x in range(2,sqt+1)]
    numd = sum(divl)*2+2
    # for the case of square triangle number
    if(abs(sqt**2 -t) <10e-6):
        numd-=1
    if(numd>=500):
        break
    n+=1
print(t)
