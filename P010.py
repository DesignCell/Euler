# Problem 10
# Summation of Primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from time import time
from math import sqrt
start = time()

def prime(cnt2):
	for cntp in range(2, (int(sqrt(cnt2)+1))):
		if cnt2 % cntp == 0:
			return False
			
def search():
	lmt=2000000 #Sum Limit
	sum_prime=0
	cnt =2
	pnum =1
	while pnum <lmt:
		if prime(cnt)!=False:
			sum_prime+=cnt
		pnum+=1
		cnt+=1
	print(sum_prime)
		
search()

print('Finished: Time ', ((time()-start)*1000),'ms')

# Sum of Primes < 2,000,000 = 142913828922 
# Solve time 48731.31ms 04-17-18