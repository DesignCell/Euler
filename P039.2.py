# Problem 039
# Integer right triangles

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#   {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximized?


from time import time
stime = time()
#import Functions # pylint: disable=import-error

# Research https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

list_trips = []
def path_triple(lim):
    for m in range(1,lim):
        for n in range(1,m):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if a+b+c > 1000: break
            list_trips.append(a+b+c)

path_triple(200)
list_trips.sort()
max_trip = 0
max_cnt = 0

for seq in list_trips:
    num = list_trips.count(seq)
    if num >= max_cnt: 
        max_trip = seq
        max_cnt = num

print(max_trip,max_cnt)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 
# Solve time: 
