# Problem 037
# Truncatable primes

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously
# remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from time import time
stime = time()
import Functions # pylint: disable=import-error



# Produce Prime Set to reference
lim = 1000000 #1m needed to produce 11. Not sure how to prove only 11.
prime_set = set()
for cnt in range(2,lim):
    if Functions.is_prime(cnt) == True: prime_set.add(cnt)
print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')
# Truncate Number Test if Prime
trunc_set = set()
for seq in prime_set:
    if len(str(seq)) == 1: continue #Eliminate single digit from sequence (2,3,5,7)
    flag = True             # Set search flag to true initailly unless not found                           
    for cnt_trunc in range(1,len(str(seq))):
        trunc_LR = int(str(seq)[cnt_trunc::]) #Truncate Left to Right
        trunc_RL = int(str(seq)[:-cnt_trunc:]) #Truncate Right to Left
        if trunc_LR not in prime_set: flag = False 
        if trunc_RL not in prime_set: flag = False
    if flag == True: trunc_set.add(seq)

# Sum Truncated Prime set
trunc_sum = 0
for seq in trunc_set:trunc_sum += seq

print(trunc_sum)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 748317
# Solve time: 9881.8ms 08-17-18


"""
Alt solution idea

loop prime numbers 2,3,5,7
2
add digit before/end.
2(1-9) & 1-9(2)
If is prime: add digit before/end.
stop when not prime not found 1-9 (if multiples found?)
loop prime number next


"""

