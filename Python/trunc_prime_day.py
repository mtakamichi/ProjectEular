def is_prime(n):
    if (n%2 == 0 and n>2) or n<=1:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    tnl= []
    lnl = list(str(n))
    for _ in range(len(lnl)-1):
        lnl.pop(0)
        tnl.extend([int(''.join(lnl))])
    return all(map(is_prime, tnl))

for y in range(2019,2050):
    for m in range(1, 12):
        for d in range(1, 31): 
            a = int(''.join(['%04d'%y, '%02d'%m, '%02d'%d]))
            if is_truncatable_prime(a):
                print('%04d'%y, '%02d'%m, '%02d'%d) 