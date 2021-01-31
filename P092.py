# Problem 092
# Square digit chains

# A number chain is created by continuously adding the square of the
# digits in a number to form a new number until it has been seen before.

# For example,
#   44 → 32 → 13 → 10 → 1 → 1
#   85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?

from time import time
stime = time()
#import Functions # pylint: disable=import-error

# Global sets
eight_nine_set = set()
one_set = set()

# Process square chain, return 1 or 89
def square_chain(num):
    if num in eight_nine_set: return 89
    if num in one_set: return 1
    if num == 89 or num == 1: return num
    new_num = 0
    for digits in map(int, str(num)): 
        new_num += digits**2
    return square_chain(new_num)

def search(lim):
    eight_nine = 0
    for cnt in range(1,lim+1):
        found = square_chain(cnt)
        if found == 1: one_set.add(cnt)
        if found == 89: 
            eight_nine_set.add(cnt) 
            eight_nine += 1
    return eight_nine   

print(search(10000000))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 8581146
# Solve time: 29644.06ms 2019.09.12

