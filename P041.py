# Problem 041
# Pandigital Primes

# We shall say that an n-digit number is pandigital if it makes use
# of all the digits 1 to n exactly once. For example, 2143 is a 4-digit
# pandigital and is also prime.

#mWhat is the largest n-digit pandigital prime that exists? 

from time import time
stime = time()
import Functions # pylint: disable=import-error
import itertools

set_perm = set()
def pan_set(d):
    pandigital = []
    for cnt in range(1,d+1):
        pandigital.append(cnt)
    permutations = set()
    permutations = itertools.permutations(pandigital,d)

    #Expensive Process ~1410ms...
    skip_set = {1,3,7,9} #skip non-primable numbers reduces overhead 50%
    for seq in permutations:
        if seq[-1] not in skip_set: continue
        set_perm.add(int("".join(map(str,seq))))

    return

max_prime = 0
#for digit in range(1,10): #~1.3s process searching 1-9 pandigital permutations
#    pan_set(digit)
#    for seq in set_perm:
#        if Functions.is_prime(seq) == True:
#            if seq > max_prime: max_prime = seq

# Since:
# 1+2+3+4+5+6+7+8+9 = 45 / 3 = 15, 9 digit pans cannot be prime
# 1+2+3+4+5+6+7+8   = 36 / 3 = 12, 8 digit pans cannot be prime
# 1+2+3+4+5+6+7     = 28 / 3 = 9.3, 7 digit pans can be prime
pan_set(7)
for seq in set_perm:
    if Functions.is_prime(seq) == True:
        if seq > max_prime: max_prime = seq

print(max_prime)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 7652413
# Solve time: 178.90ms 09-18-18
