# Problem 27
# Quadratic primes
 
# Euler discovered the remarkable quadratic formula: n2+n+41
# It turns out that the formula will produce 40 primes for the
# consecutive integer values 0≤n≤39. However,
# when n=40,402+40+41=40(40+1)+41 is divisible by 41,
# and certainly when n=41,412+41+41 is clearly divisible by 41.

# The incredible formula n2−79n+1601 was discovered,
# which produces 80 primes for the consecutive values 0≤n≤79.
# The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form: n2+an+b
#   where |a|<1000 and |b|≤1000
alim = 1000
blim = alim+1
#   where |n| is the modulus/absolute value of n
#   e.g. |11|=11 and |−4|=4

# Find the product of the coefficients, a and b, for the quadratic
# expression that produces the maximum number of primes for consecutive
# values of n, starting with n=0.

from time import time
stime = time()
import Functions # pylint: disable=import-error

def consecutive_primes(num_a,num_b): # Returns consecutive prime count
    cnt = 0
    prime = True
    while prime == True:
        quad = cnt**2 + num_a * cnt + num_b
        prime = Functions.is_prime(abs(quad))
        if prime == True:  cnt+=1 #Includes Zero
    return cnt

product = 0
num_primes = 0
temp_primes = 0
for cnt_a in range(-alim+1,alim):
    for cnt_b in range(-blim+1,blim):
        temp_primes = consecutive_primes(cnt_a,cnt_b)
        #print(cnt_a,cnt_b,temp_primes)
        if temp_primes > num_primes:
            num_primes = temp_primes
            product = cnt_a * cnt_b
            #print(num_primes,product)
    #if cnt_a%10 == 0:   print(int(cnt_a/10),'%') # Status

print(num_primes, product)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: -59231 with 71 consecutive prims
# Solve time: 8955.94ms 06-11-18