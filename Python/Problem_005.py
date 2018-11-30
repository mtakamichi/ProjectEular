# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import numpy as np
import math

# is_prime
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

N = 20
Nl = np.arange(2, N+1, dtype=np.int64)
Nl = Nl[:, np.newaxis]
is_vprime = np.vectorize(is_prime)
pl = np.extract(is_vprime(Nl),Nl)
pl = pl[np.newaxis, :]

emax = 1
while 2**(emax+1) < N:
    emax += 1

ml = np.zeros([emax, N-1, pl.size], dtype=np.int64);
for i in range(emax):
     ml[i,:,:] = (Nl % (pl**(i+1)))  < 1

pel = np.max(np.sum(ml,axis=0),axis=0)
np.power(pl,pel)
ans = np.prod(np.power(pl,pel))
print(ans)
