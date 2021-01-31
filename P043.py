# Problem 043
# Sub-String Divisibility

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#   d2d3d4=406 is divisible by 2
#   d3d4d5=063 is divisible by 3
#   d4d5d6=635 is divisible by 5
#   d5d6d7=357 is divisible by 7
#   d6d7d8=572 is divisible by 11
#   d7d8d9=728 is divisible by 13
#   d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

from time import time
stime = time()
#import Functions # pylint: disable=import-error
import itertools

set_perm = set()
def perm_funct():
    
    pandigital = []
    for cnt in range(0,10):
        pandigital.append(cnt)
    permutations = set()
    permutations = itertools.permutations(pandigital,10)
    for seq in permutations:
        if seq[0] == '0': continue
        seq_temp = int("".join(map(str,seq)))
        if digit_div(seq_temp) == True: set_perm.add(seq_temp)


def digit_div(num):
    div = [2,3,5,7,11,13,17] # Divisible sequence
    for cnt in range(1,8): #  1-7 digit sequence
        if int(str(num)[cnt:cnt+3:]) % div[cnt-1] != 0: return False
    return True

perm_funct()
sum_num = 0
for seq in set_perm:
    sum_num += seq

print(sum_num)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 16695334890
# Solve time: 17120.59ms 09-21-18
