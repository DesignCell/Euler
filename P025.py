from time import time
stime = time()

# Problem 25
#
"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
fib_list = [1,1]

def fib_calc(i):
    fib_list.append(fib_list[i-3]+fib_list[i-2])
    return

cnt = 2 # starting after fib1 & fib2 already set in list minus the start offset of 1
stop = False
fib_len = 0

while stop == False:
    cnt += 1
    fib_calc(cnt)
    fib_len = len(str(fib_list[cnt-1]))
    if fib_len == 1000:
        print(cnt, fib_len)
        stop = True


print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 4782
# Solve time: 129.6ms 05-21-18