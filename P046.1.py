# Problem 046
# Goldbach's other conjecture

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#   9 = 7 + 2×12
#   15 = 7 + 2×22
#   21 = 3 + 2×32
#   25 = 7 + 2×32
#   27 = 19 + 2×22
#   33 = 31 + 2×12

# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from time import time
stime = time()
import Functions # pylint: disable=import-error

square = []
def square_list():
    lim = 55
    for cnt in range(1,lim+1):
        square.append(2*cnt**2)
    return

def search():
    cnt = 7
    while True:
        cnt += 2
        if Functions.is_prime(cnt) == True: continue
        flag = False
        for num in range(cnt-2,0,-2):
            if Functions.is_prime(num) == True:
                for seq in square:
                    if num + seq == cnt: flag = True
                #lim = int((cnt/2)**.5)
                #for seq in range(lim,0,-1):
                #    if num + 2*seq**2 == cnt: flag = True
        if flag == False: 
            print(cnt, num)
            return cnt

square_list()
print(search())


print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution  : 5777
# Solve time: 17981.57ms with adapted no guessing...
# Solve time: 9383.64ms with ranged iteration...
