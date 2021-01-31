# Problem 056
# Powerful Digit Sum

# A googol (10**100) is a massive number: one followed by one-hundred zeros;
# 100**100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?

from time import time
stime = time()
#import Functions # pylint: disable=import-error


def pwr_sum(a,b):
    num = a ** b
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit)
    return digit_sum

def run(lim):
    max_digit_sum = 0
    for a in range(1,lim+1):
        for b in range(1,lim+1):
            temp = pwr_sum(a,b)
            if temp > max_digit_sum: max_digit_sum = temp
    return max_digit_sum

print(run(100))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 972
# Solve time: 224.93 2019.08.05

