# Problem 048
# Self Powers

# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

from time import time
stime = time()
#import Functions # pylint: disable=import-error
from sys import setrecursionlimit
setrecursionlimit(1100) # just above target number

def recur_power(n):
   if n == 1:
       return n
   else:
       return n**n + recur_power(n-1)



print(str(recur_power(1000))[-10:])

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 9110846700
# Solve time: 36.43ms 11-15-18
