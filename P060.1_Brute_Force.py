# Problem 060
# Prime pair sets

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them
# in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from time import time
stime = time()
import Functions # pylint: disable=import-error
from itertools import combinations


def search(lim):
    p_list = Functions.primes_sieve(lim) #Start with prime list to limit argument
    print('p_list',len(p_list),round(((time() - stime) * 1000), 2), 'ms')

    for num_1 in p_list:
        for num_2 in p_list:
            if num_2 < num_1: continue
            if cat_prime((num_1,num_2)) == True: 
                for num_3 in p_list:
                    if num_3 < num_2: continue
                    if cat_prime((num_1,num_3)) == True:
                        if cat_prime((num_2, num_3)) == True:
                            for num_4 in p_list:
                                if num_4 < num_3: continue
                                if cat_prime((num_1,num_4)) == True:
                                    if cat_prime((num_2,num_4)) == True:
                                        if cat_prime((num_3,num_4)) == True:
                                            for num_5 in p_list:
                                                if num_5 < num_4: continue
                                                if cat_prime((num_1,num_5)) == True:
                                                    if cat_prime((num_2,num_5)) == True:
                                                        if cat_prime((num_3,num_5)) == True:
                                                            if cat_prime((num_4,num_5)) == True: 
                                                                print(set_sum((num_1,num_2,num_3,num_4,num_5)),num_1,num_2,num_3,num_4,num_5)        
                                                                return

    return


def cat_prime(two_primes): #test if two numbers concatenated together X+Y and Y+X is prime
    if Functions.is_prime(int(str(two_primes[0]) + str(two_primes[1]))) == True:
        if Functions.is_prime(int(str(two_primes[1]) + str(two_primes[0]))) == True: return True
    return

def test_seq(comb_seq):
    pair_comb = [x for x in combinations(comb_seq,2)]
    for cat_test in pair_comb:
            if cat_prime(cat_test) != True: return False
    print(set_sum(comb_seq), comb_seq)
    return True

def set_sum(nums):
    cnt = 0
    for num in nums: cnt += num
    return cnt       

search(10000) # Assumed

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 26033 (Limit 10k)
# Solve time: 20945.14ms 2019.10.01

# Solution	: 26033 (Limit 30k)
# Solve time: 20945.14ms 2019.10.01