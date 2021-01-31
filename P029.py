# Problem 29
# Distinct Powers

from time import time
stime = time()
#import Functions # pylint: disable=import-error

 
ab = 100
dist_set = set()

for cnt_a in range(2,ab+1):
    for cnt_b in range(2, ab+1):
        dist_set.add(cnt_a ** cnt_b)

print(len(dist_set))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 9183
# Solve time: 13.33ms 06-11-18