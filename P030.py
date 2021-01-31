# Problem 30
# Digit fifth powers
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

from time import time
stime = time()
#import Functions # pylint: disable=import-error

pwr = 5
digit_set = set()
for cnt in range(2,1000000):
    digit_pwr = 0
    if len(str(cnt)) >=1:   digit_pwr += int(str(cnt)[0:1:])**pwr
    if len(str(cnt)) >=2:   digit_pwr += int(str(cnt)[1:2:])**pwr
    if len(str(cnt)) >=3:   digit_pwr += int(str(cnt)[2:3:])**pwr
    if len(str(cnt)) >=4:   digit_pwr += int(str(cnt)[3:4:])**pwr
    if len(str(cnt)) >=5:   digit_pwr += int(str(cnt)[4:5:])**pwr
    if len(str(cnt)) >=6:   digit_pwr += int(str(cnt)[5:6:])**pwr
        
    if cnt == digit_pwr: 
        digit_set.add(cnt)
        print(cnt)

print(sum(digit_set))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 443839
# Solve time: 7887.36ms 06-12-18