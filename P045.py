# Problem 045
# Triangular, pentagonal, and hexagonal

# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

#   Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#   Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
#   Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

from time import time
stime = time()
#import Functions # pylint: disable=import-error

def pent_check(value):
    pent_num = (1 + (1 + 24 * value)**.5 ) / 6
    if pent_num.is_integer() == True:   return True
    return False

def searchHex():
    n = 285 # Find the next TPH number
    while True:
        n += 1
        Hn = n*(2*n-1)
        if pent_check(Hn) == True:  return Hn

print(searchHex())

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution  : 1533776805
# Solve time: 25.45ms 09-26-18
