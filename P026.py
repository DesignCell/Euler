from time import time
stime = time()
#import Functions # pylint: disable=import-error
import decimal

# Problem 26
# Reciprocal Cycles

#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def Reciprocal(cnt,precision):
    decimal.getcontext().prec = precision*2
    num_str = str(decimal.Decimal(1) / decimal.Decimal(cnt))
    num_str = num_str[2::]
    for cnt_start in range(0,10):
        for cnt_size in range(1,precision):
            if num_str[cnt_start:cnt_start + cnt_size:] == '':  return 0
            if num_str[cnt_start:cnt_start + cnt_size:] == num_str[cnt_start + cnt_size:cnt_start + cnt_size*2:] and num_str[cnt_start:cnt_start + cnt_size:] == num_str[cnt_start + cnt_size*2:cnt_start + cnt_size*3:]:
                return cnt_size
    return -1

rec_max = 0
rec_max_cnt = 0
rec_set = set()
rec_prec = [20,250,500,2000,5000]
for cnt in range(1,1001):
    if cnt in rec_set: break
    for cnt_prec in rec_prec: 
        if cnt in rec_set: break
        rec_return = Reciprocal(cnt,cnt_prec) 
        if rec_return != -1:
            rec_set.add(cnt)
            if rec_return > rec_max:   
                rec_max = rec_return
                rec_max_cnt = cnt
             
print(rec_max_cnt,rec_max)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: d = 983 cnt = 982 recipricating
# Solve time: 702.74ms 06-08-18