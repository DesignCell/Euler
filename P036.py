# Problem 036
# Double-base palindromes

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from time import time
stime = time()
import Functions # pylint: disable=import-error


cnt_pal = 0
lim = 1000000

for cnt in range(lim):
    if Functions.palindrome(cnt) == True: #Call function palidrone, returns true is it is
        bnum = str(bin(cnt))[2::]
        if bnum[0:1:] == '0': continue
        if Functions.palindrome(bnum) == True: 
            cnt_pal += cnt

print(cnt_pal)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 872187
# Solve time: 703.25ms 08-12-18