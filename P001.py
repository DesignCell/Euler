# Problem 1
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

from time import time
start = time()

# sumnum=0
# for num in range(1,1000):
# 	if num%3==0 or num%5==0: sumnum+=num
# print ('Sum of all the multiples of 3 or 5 below 1000 = '+str(sumnum))



# Sum of all the multiples of 3 or 5 below 1000 = 233168
# Solve Time: 0.494ms


def search(lim):
    sumnum=0
    for num in range(1,lim):
        if num%3==0 or num%5==0:    sumnum+=num
    return str(sumnum)

print(search(1000))

print('Finished: Time ', ((time()-start)*1000),'ms')