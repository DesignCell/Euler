# Problem 6
# Sum Square Difference
# The sum of the squares of the first ten natural numbers is,
#				12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#				(1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.



from time import time
start = time()

numsumsq = 0
numsqsum = 0

for cnt in range(1,101):
	print(str(cnt),'	',str(numsumsq),'		',str(numsqsum**2))
	numsumsq+=cnt**2
	numsqsum+=cnt
	print(str(cnt),'	',str(numsumsq),'		',str(numsqsum**2))

print('Difference = ', str(numsqsum**2 - numsumsq))

print('Finished: Time ', ((time()-start)*1000),'ms')

# Differnce of sumSq and SqSum of 1-100 = 25164150
# Solve time 13.52ms 04-16-18