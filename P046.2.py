# Problem 046
# Goldbach's other conjecture

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#   9 = 7 + 2×12
#   15 = 7 + 2×22
#   21 = 3 + 2×32
#   25 = 7 + 2×32
#   27 = 19 + 2×22
#   33 = 31 + 2×12

# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from time import time
stime = time()
import Functions # pylint: disable=import-error


def isDsq( n ):
    x = int((n/2)**.5)
    if n == (x*x)*2:
        return 1

def search():
    prime_list = [2,3,5,7]
    cnt = 7
    while True:
        cnt += 2
        if Functions.is_prime(cnt) == True:
            prime_list.append(cnt)
            continue
        flag = False
        for num in reversed(prime_list):
            if isDsq(cnt-num) == True: flag = True
        if flag == False: 
            print(cnt)
            return cnt

#square_list()
print(search())


print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution  : 5777
# Solve time: 559.96ms 09/28/18