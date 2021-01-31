# Problem 3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from time import time
start = time()

factor = 600851475143
from math import sqrt

def prime(cnt2):
	for cntp in range(2, (int(sqrt(cnt2)))):
		if cnt2 % cntp == 0:
			return False

start = time()
for cnt1 in range(2, (int(sqrt(factor)))):
	if factor % cnt1 == 0:
		if prime(cnt1) != False:
			print('Prime Factor ' + str(cnt1))

print('Finished: Time ', ((time()-start)*1000),'ms')

# Prime Factor: 6857
# Solve time 298ms 04-12-18