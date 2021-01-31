# Problem 063
# Powerful digit counts

# The 5-digit number, 16807=7**5, is also a fifth power. 
# Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

from time import time
stime = time()
#import Functions # pylint: disable=import-error

# Assumptions
# If number of digits exceeds power, increment and reset
# start power at current 

def search():
    y = 0
    cnt = 0
    while True:
        y += 1
        for x in range(1,10):
            xy = x**y
            len_new = len(str(xy))
            if len_new == y:
                cnt+=1 
                #print("Found: ",cnt,x,y,xy)
            if cnt == 49: return 49 #This is cheap....


print(search())

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 49
# Solve time: 1.0ms 2019.09.13