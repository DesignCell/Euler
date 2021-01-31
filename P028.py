# Problem 28
# Number spiral diagonals

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
"""
        (21) 22  23  24 (25)
         20  (7)  8  (9) 10
         19   6  (1)  2  11
         18  (5)  4  (3) 12
        (17) 16  15  14 (13)
"""
# It can be verified that the sum of the numbers on the diagonals is 101.
# (1) 2 (3) 4 (5) 6 (7) 8 (9) 10 11 12 (13) 14 15 16 (17) 18 19 20 (21) 22 23 24 (25) 26 27 28 29 30 (31)
# 1+2+2+2+2+4+4+4+4+
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

from time import time
stime = time()
#import Functions # pylint: disable=import-error

def spiral_count(lim): #Imput as XY size of spiral grid, returns sum of pattern Ep027
    total = 1
    cnt_diag = 1
    for cnt_sprial in range(2,lim+1,2):
        for cnt_seq in range(4):
            total += cnt_sprial
            cnt_diag += total
    return cnt_diag

print(spiral_count(1001))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 669171001
# Solve time: 1.02ms 06-11-18