# Problem 052
# Permuted Multiples

# It can be seen that the number, 125874, and its double, 251748, 
# contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that
# 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from time import time
stime = time()
#import Functions # pylint: disable=import-error

def search(lim):
    num = 1
    while True:
        num+=1
        if test(num,lim) == True:
            print(num)
            break

def test(num,lim):
    test_set_1 = set()
    test_set_2 = set()
    #lim = 2

    #Set the digits of num into test_set_1
    for digit in str(num): test_set_1.add(digit)

    #loop to limit of multipls    
    for cnt in range(2,lim+1):
        test_set_2.clear()
        for seq in test_set_1: test_set_2.add(seq) #reset duplicated set
        for digit in str(cnt*num): 
            if digit not in test_set_2: 
                return False
            else:
                test_set_2.remove(digit)
    return True

search(6)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# 2x =  125874 350.11ms
# 3x =  142857 393.67ms
# 4x =  142857 406.57ms
# 5x =  142857 387.41ms
# 6x =  142857 386.58ms
# Solution	: 142857
# Solve time: 386.58ms
