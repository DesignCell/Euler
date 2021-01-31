# Problem 050
# Consecutive Prime Sum

# The prime 41, can be written as the sum of six consecutive primes:
#       41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from time import time
stime = time()
import Functions # pylint: disable=import-error

def search_sum(lim):
    prime_list_sum = primes_sieve_sum(lim)
    prime_list = Functions.primes_sieve(lim)
    con_max = 0
    con_max_cnt = 0
    for cnt1 in range(0,len(prime_list_sum)):
        con_sum = prime_list_sum[cnt1]
        con_cnt = 1
        for cnt2 in range(cnt1+1,len(prime_list_sum)):
            con_sum += prime_list_sum[cnt2]
            con_cnt += 1    
            if con_cnt > con_max_cnt: #ingnor if not higher
                if con_sum in prime_list: #if higher consecutive then start checking for prime
                    con_max_cnt = con_cnt
                    con_max = con_sum 
        
    print(con_max) #print Answer

def primes_sieve_sum(limit): 
    #Returns list of primes up to including argument
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
   
    #Consecutive Sum Limit 
    con_sum = 0
    for seq in primes:
        if con_sum < limit+1 and primes[seq] == True: 
            con_sum += seq
            sum_limit = seq
        elif con_sum > limit: break
        
    return [i for i in primes if primes[i]==True and i < sum_limit]

search_sum(1000000)


print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 997651
# Solve time: 8566.54ms 11/30/18
