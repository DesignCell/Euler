from time import time
stime = time()

# Problem 23
# Non-Abundant Sums

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
# as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater 
# than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any
# further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two
# abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Determin factors of given number and return sum
def factor_sum(num):
    sfact = set()
    sfact.add(1) #add (1) as starting factor not tested to eliminate input number return
    for cnt in range(2, int(num**0.5)+1):
        if num%cnt == 0:
            sfact.add(cnt)
            if num/cnt != cnt: 
                sfact.add(num/cnt)
    return int(sum(sfact))

#compile list of all abundant numbers from 1 - 28124
lim = 28124 #28123 + 1 to include
#lim = 100
abundant_num = set()
for cnt in range(1,lim):
    if factor_sum(cnt) > cnt:
        abundant_num.add(cnt)
print('Abundant Sum List Compiled:',len(abundant_num))
#print(abundant_num)

#Find all abundant pair sums < lim
abundant_pair = set()
abundant_sum = 0
for seq1 in abundant_num:
    #print(seq1)
    for seq2 in abundant_num:
        if seq2 < seq1: continue
        abundant_sum = seq1 + seq2
        if abundant_sum > lim:   break
        #if abundant_sum in abundant_pair: continue
        #print(seq1, seq2)
        abundant_pair.add(seq1 + seq2)
print('Abundant Pair Sums Compiled:', len(abundant_pair))
#print(abundant_pair)

# Flip abundant pair list into non-abundant numbers
sum_nabu = 0
for test_int in range(1,lim):
    if test_int in abundant_pair: continue
    sum_nabu += test_int
    
print('Sum of all non-abundant intengers less than ', lim,':',sum_nabu)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 4179871
# Solve time: 117299.79 05/18/18
# Solve time: 28118.8 (Repl.it) 05/18/18