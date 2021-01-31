from time import time
stime = time()

# Problem 21
# Amicable Numbers

# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are
# an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def divisors(num):
    sum_num = 0
    for cnt in range(1,int(num/2)+1):
        if num%cnt == 0:
            sum_num += cnt
    return sum_num
limit = 10000
amicable = []
for seq in range(1,limit):
    if seq not in amicable:
        div1 = divisors(seq)
        div2 = divisors(div1)
        if div2 == seq and div1 != div2:
            amicable.append(seq)
            amicable.append(div1)
            print(seq,div1)
            
print(sum(amicable))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 31626
# Solve time: 5739.4ms 05-13-18