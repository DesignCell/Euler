# Problem 20
# Factorial Digit Sum

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

from time import time
stime = time()

lim = 100
num = lim
sum_digit = 0

for cnt in range(lim, 1, -1):
	num *= (cnt - 1)
for cnt2 in range(0,int(len(str(num)))):
	sum_digit += int(str(num)[cnt2])
	
print(sum_digit)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 648
# Solve time: 0.57 04-27-18
