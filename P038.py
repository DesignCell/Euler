# Problem 038
# Pandigital Multiples

# Take the number 192 and multiply it by each of 1, 2, and 3:
#   192 × 1 = 192
#   192 × 2 = 384
#   192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
# and 5, giving the pandigital, 918273645, which is the concatenated product 
# of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed
# as the concatenated product of an integer with (1,2, ... , n) where n > 1?

from time import time
stime = time()
#import Functions # pylint: disable=import-error

import itertools

pandigital = [1,2,3,4,5,6,7,8,9]
permutations = set()
permutations = itertools.permutations(pandigital,9)

#Expensive Process ~1410ms...
set_perm = set()
for seq in permutations: 
    set_perm.add(int("".join(map(str,seq))))

def mult(num):
    cnt = 1
    con_mult = str(num)
    while len(con_mult) < 9:
        cnt += 1
        con_mult += str(num*cnt)
        if len(con_mult) == 9: return int(con_mult)
    return

lim = 9999 # through iterative search: while cnt+cnt*2 > 9 digits
for cnt in range(1,lim):
    if mult(cnt) in set_perm:   print(cnt,mult(cnt))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: num 9327 solves 932718654
# Solve time: 1477.19ms 09-12-18
