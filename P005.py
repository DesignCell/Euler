# Problem 5
# Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

# 11*12*13*14*15*16*17*18*19*20=670442572800 GCM
# True div scan 0.05 - 0.15ms * 670442572800 ~=63years to search full range...

from time import time
start = time()

gcm = 670442572800

def div(num):
	for cnt in range(19,10,-1):
		if num%cnt!=0:
			return False

def search():
	for mult in range(20,gcm,20):
		if div(mult)!=False:
			return mult
		
print (str(search()))

print('Finished: Time ', ((time()-start)*1000),'ms')

# Smallest divisible by all 1-20 = 232792560
# Solve time 18481.94ms 04-17-18