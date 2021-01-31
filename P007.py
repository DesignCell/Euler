# Problem 7
# 10,001st Prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?


from time import time
from math import sqrt
start = time()


def prime(cnt2):
	for cntp in range(2, (int(sqrt(cnt2)+1))):
		if cnt2 % cntp == 0:
			return False
			
def search():
	top=10001 #Search for Nth Prime
	
	cnt =3
	pnum =1
	while pnum <top:
		if prime(cnt)!=False:
			pnum+=1
			if pnum == top:
				print (str(pnum),'	',str(cnt))
		cnt+=2
		
search()

print('Finished: Time ', ((time()-start)*1000),'ms')

# 10,001st Prime = 104743 
# Solve time 782.33ms 04/17/18