# Problem 057
# Square root convergents

# See attached image
# a + n / d
# a * d + n


from time import time
stime = time()
#import Functions # pylint: disable=import-error

def finite_con_fract(lim): 
    nd_cnt = 0 
    for cnt in range(lim, -1,-1):
        fraction_list = rollup_iter(cnt)
        if len(str(fraction_list[0])) > len(str(fraction_list[1])): nd_cnt += 1
    return nd_cnt

def rollup_iter(lim):
    n = 1
    d = 2
    for cnt in range(lim-1,-1,-1):
        if cnt == 0: a = 1
        else: a = 2
        n_ = d
        d = d * a + n
        n = n_
    return d,n

print(finite_con_fract(1000))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 153
# Solve time: 199.37 ms 2019.08.08

