# Problem 034
# Digit factorials

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from time import time
stime = time()
import Functions # pylint: disable=import-error

# Product list of factorials 1-9 for reference
#                 0  1  2  3   4    5    6     7      8       9
fact_list = [] # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
for cnt in range(0,10): fact_list.append(Functions.factorial(cnt))
# 7 digits of 9! = 2540160 less than 9999999. 2540160 upper count limit
lim = 2540160 #1500ms
lim = 99999   # 275ms
answer = 0
cnt = 3 # 1! & 2! not counted as they are not be sums
while cnt < lim:
    cnt += 1
    sum_fact = 0

    for cnt_digit in range(1,len(str(cnt))+1):
        
        digit = int(str(cnt)[-cnt_digit])
        sum_fact += fact_list[digit]

        #if sum_fact > cnt and : break

    if sum_fact == cnt: answer += sum_fact
    elif sum_fact > cnt:
        cnt += 9 - cnt%10

print(answer)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 40730
# Solve time: 275.88ms 06-29-18