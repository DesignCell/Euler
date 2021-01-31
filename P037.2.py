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

def primeLR(num): #Buil numbers left to right
    truncLR_prime(num)
    for seq in 1,3,7,9: #End of number must not be even or div by 5
        a = num*10 + seq
        if Functions.is_prime(a) == True: 
            primeLR(a)

def truncLR_prime(trunc):   
    if trunc < 10: return       
    for cnt_trunc in range(1,len(str(trunc))):
        trunc_LR = int(str(trunc)[cnt_trunc::]) #Truncate Left to Right
        if Functions.is_prime(trunc_LR) == False: return
    print(trunc)
    ptrunc_sum[0] += trunc

ptrunc_sum = [0]
for cnt in 2,3,5,7: #prime initializers
    primeLR(cnt)
print('Solution: ',ptrunc_sum)



print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 748317
# Solve time: 9881.8ms 08-17-18
# Solve time: 20.28ms  09-10-18


