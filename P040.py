# Problem 040
# Champernowne's constant

from time import time
stime = time()
#import Functions # pylint: disable=import-error

conc_num = ""
cnt = 0 #Omit the first to offest the string

while len(conc_num) <= 1000000:
    conc_num += str(cnt)
    cnt += 1

p040 = 1 #Set to d1
for mult in range(1,7,): #starting with d10
    offset_mult = 10**mult
    print(offset_mult)

    p040 *= int(conc_num[offset_mult:offset_mult+1:])

print(p040)


print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 210
# Solve time: 344.17ms 09-17-18
# Solve time: 88.09ms 2019.09.28 Ryzen7/32gb
