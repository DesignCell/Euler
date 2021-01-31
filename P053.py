# Problem 053
# Combinatoric selections

# See image

from time import time
stime = time()
import Functions # pylint: disable=import-error

def comb_equ(n,r):
    n_ = Functions.factorial(n)
    r_ = Functions.factorial(r)
    n_r = Functions.factorial(n-r)
    return n_ / (r_ * n_r)

def search(lim):
    exceeds = 1000000
    e_cnt = 0
    for cnt1 in range(1,lim+1):
        for cnt2 in range(1, cnt1+1):
            if comb_equ(cnt1,cnt2) >= exceeds: e_cnt += 1
    return e_cnt

print(search(100))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 4075
# Solve time: 175.9ms 2019.07.07
