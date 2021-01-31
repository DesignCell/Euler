# Problem 32
# Pandigital products

# We shall say that an n-digit number is pandigital if it makes use of all the digits 
# 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
#  multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written
# as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be
# sure to only include it once in your sum.

from time import time
stime = time()
#import Functions # pylint: disable=import-error
import itertools

pandigital = [1,2,3,4,5,6,7,8,9]
permutations = set()
permutations = itertools.permutations(pandigital,9)

set_perm = set()

for seq in permutations: 
    seq_perm = "".join(map(str,seq))
    for mult1 in range(1,3):
        for mult2 in range(3,5):
            #if mult1 + mult2 > 6:   pass
            if int(seq_perm[0:mult1:]) * int(seq_perm[mult1:mult1+mult2:]) == int(seq_perm[mult1+mult2::]):
                set_perm.add(int(seq_perm[mult1+mult2::]))
                
prod_perm = 0
for prod_seq in set_perm: prod_perm += prod_seq

print(prod_perm)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 45228
# Solve time: 4507.71ms 06-21-18