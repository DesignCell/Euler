# Problem 097
# Large non-Mersenne prime

# digits: 28433×2**7830457+1.

# Find the last ten digits of this prime number.


from time import time
stime = time()
#import Functions # pylint: disable=import-error

num = str(28433*(2**7830457)+1)
print(num[-10:])

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 8739992577
# Solve time: 73405.97ms 2019.09.12

