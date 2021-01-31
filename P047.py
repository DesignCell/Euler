# Problem 047
# Distinct primes factors

# The first two consecutive numbers to have two distinct prime factors are:
#   14 = 2 × 7
#   15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
#   644 = 2² × 7 × 23
#   645 = 3 × 5 × 43
#   646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

from time import time
stime = time()
#import Functions # pylint: disable=import-error

p_list = [2] #initialize with first prime != 1
def prime_seive(lim):
    global p_list
    p_list += [num for num in range(3,lim+1,2)]

    for cnt in range(3,int(lim**2)+1):
        x = 2
        while cnt * x <= lim:
            temp = cnt * x
            if temp in p_list:   p_list.remove(cnt * x)
            x +=1
    return p_list

def distinct_factors(num):
    pass
    test = num
    d_fact = set()
    for seq in p_list:
        if seq > test: break # skip if division is already greater than test number reduction
        while test % seq == 0:  
            d_fact.add(seq)
            test = test / seq
    return  len(d_fact)

def distinct_search(search):
    # search = number of distinct primes in factors
    tally = 0
    prime_seive(1000) # iterated
    # 2 * 3 * 5 * 7 = 210
    for cnt in range(210,200000):
        if distinct_factors(cnt) == search:
            tally +=1
        else:
            tally = 0
        if tally == search: return cnt - search + 1
    return

print(distinct_search(4))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 134043
# Solve time: 2823.81ms 11-15-18
