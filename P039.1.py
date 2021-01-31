# Problem 039
# Integer right triangles

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#   {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximized?


from time import time
stime = time()
from math import sqrt
#import Functions # pylint: disable=import-error

# Brute Force Method

def pathagoren(p):
    cnt = 0
    for a in range(2,int(p/2)+1,2):
        for b in range(2,int(p/2)+1,2):
            c = sqrt(a*a + b*b)
            if a+b+c == p: cnt += 1
            if a+b+c > p: break
    return int(cnt/2)

def cnt_p():
    maximized = 0
    for p in range(2,1001,2):
        maximized_test = pathagoren(p)
        if maximized_test >= maximized: 
            maximized = maximized_test
            print(p, maximized)
cnt_p()

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 840 solving 8 permentations
# Solve time: 5248.44ms 09-16-18
