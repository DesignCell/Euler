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

def search(lim,sets):
    p_list = Functions.primes_sieve(lim) #Start with prime list to limit argument
    print('p_list',round(((time() - stime) * 1000), 2), 'ms')
    cp_list = [x for x in combinations(p_list,2) if cat_prime(x)== True] #Filter 2 combinations of concatenatable primes.
    print('cp_list',round(((time() - stime) * 1000), 2), 'ms')
    sort_dict = sort(cp_list) # Create dictionary of key [set of concatenatable primes]
    print('sort_dict',round(((time() - stime) * 1000), 2), 'ms')

    dict_comb = combinations(sort_dict.keys(),sets)
    print('dict_comb',round(((time() - stime) * 1000), 2), 'ms')

    for seq in dict_comb:
        #Convert tuple seq in to set
        seq_set = set()
        for seqseq in seq: seq_set.add(seqseq)

        #Cycle through all tuple seq items to confirm is subset, False breaks
        for cnt in range(sets):
            if seq_set.issubset(sort_dict[seq[cnt]]) == False: 
                break
        else: 
            return [set_sum(seq),seq]

    return False

def cat_prime(two_primes): #test if two numbers concatenated together X+Y and Y+X is prime
    if Functions.is_prime(int(str(two_primes[0]) + str(two_primes[1]))) == True:
        if Functions.is_prime(int(str(two_primes[1]) + str(two_primes[0]))) == True: return True
    return

def sort(in_list):
    sort_dict = {}
    for seq in in_list:
        # First checks add 0,1
        if seq[0] not in sort_dict:
            sort_dict[seq[0]] = {seq[0],seq[1]} #If new to dict, then add Key:Set Value
        else:
            sort_dict[seq[0]].add(seq[1]) #If not new, add to set
        # Second checks add 1,0
        if seq[1] not in sort_dict:
            sort_dict[seq[1]] = {seq[0],seq[1]} #If new to dict, then add Key:Set Value
        else:
            sort_dict[seq[1]].add(seq[0]) #If not new, add to set
    return  sort_dict

def set_sum(nums):
    cnt = 0
    for num in nums: cnt += num
    return cnt       

print(search(1000,3))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 
# Solve time: 
