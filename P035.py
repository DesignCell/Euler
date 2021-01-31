# Problem 035
# Circular primes

# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

from time import time
stime = time()
import Functions # pylint: disable=import-error

lim = 1000000
set_prime = set()
set_prime.add(2)
set_circle = set()

def in_set(set_check,set_test): #iterate test in check return false if not found, else return true
    for seq in set_test: 
        if seq not in set_check:    return False
    return True

for cnt in range(3,lim+1,2): #Find all primes below limit
    if Functions.is_prime(cnt) == True:
        set_prime.add(cnt)

print(len(set_prime),'Primes')

for seq in set_prime:   #sequence through primes to index digits
    if seq in set_circle:   continue # if cirlce found
    if len(str(seq)) == 1:  # skip if 1-9
        set_circle.add(seq)
        continue
    
    #index set and add current
    set_seq_index = set()
    set_seq_index.add(seq)
    seq_temp = seq
    
    for cnt in range(1,len(str(seq))): #index number of digits less 1
        seq_indexed = str(seq_temp)[1::]   #splice 2nd digit to end
        seq_indexed += str(seq_temp)[0:1:] #con. first to last
        set_seq_index.add(int(seq_indexed))
        seq_temp = seq_indexed
    if in_set(set_prime,set_seq_index) == True: set_circle = set_circle | set_seq_index
               
print(len(set_circle))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 55
# Solve time: 12384.1ms 07-14-18