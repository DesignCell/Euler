# Problem 058
# Spiral Primes

# See reference

#     |  |     |     |           |     |           |     |           |                 |     |                 |           |     |           |                 |                 |     |                 |           |     |                 |    
# 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80
#  C     |     |     |     |           |           |           |           |                 |                 |                 |                 |
#      +02   +02   +02   +02         +04         +04         +04         +04               +06               +06               +06               +06                     +08 
#        T     T     T                 T           T                                         T                 T                 T                
# Loop + (4) times, add 2 for next cycle: 2,4,6,... 
#      
from time import time
stime = time()
import Functions # pylint: disable=import-error

def spiral():
    cnt = 1
    n = 0
    d = 0
    ratio = 1
    incr = 0
    while ratio > .1:
        incr += 2
        for cnt_c in range(4):
            cnt += incr
            if Functions.is_prime(cnt) == True: n += 1
            d += 1
        ratio = n/d
    return incr + 1

print(spiral())

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 26241
# Solve time: 19762.56 ms 2019.08.09

