# Problem 049
# Prime Permutations

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: 
#       (i)  each of the three terms are prime
#       (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

from time import time
stime = time()
import Functions # pylint: disable=import-error
import itertools


def search():
    plist = Functions.primes_sieve(9999) # 4 digits limit
    skip_set = {1487, 4817, 8147}
    for seq in plist:
        if seq < 1000: continue # 4 digit limit
        if seq in skip_set: continue # skip 1487, 4817, 8147
        seq_str = str(seq) # move sequence to string
        perm_set = set()
        for seq_per in itertools.permutations(seq_str,len(seq_str)):
            seq_per = int("".join(seq_per))
            if seq_per not in plist: continue
            elif seq_per > seq: perm_set.add(seq_per)
        for seq_diff in perm_set:
            diff = seq_diff - seq
            if diff > 5000: continue # 
            if seq + diff in perm_set: 
                if seq + diff + diff in perm_set: print(str(seq)+str(seq+diff)+str(seq+diff+diff))



search()
#test_search(1487)


print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 296962999629
# Solve time: 401.77ms 11/20/18
