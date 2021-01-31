# Problem 16
# Power Digit Sum

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

from time import time
stime = time()

num = 2**1000
sum_num = 0
lim = len(str(num))

for cnt in range(0, lim):
	sum_num += int(str(num)[cnt])

print('Solution: ', sum_num)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 1366
# Solve time: 1.29ms 04-25-18