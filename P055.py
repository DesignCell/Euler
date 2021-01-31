# Problem 055
# Lychrel Numbers

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
# Not all numbers produce palindromes so quickly. For example,

#    349 +  943 = 1292,
#   1292 + 2921 = 4213
#   4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.
# Although no one has proved it yet, it is thought that some numbers,
# like 196, never produce a palindrome. A number that never forms a palindrome 
# through the reverse and add process is called a Lychrel number. 
# Due to the theoretical nature of these numbers, and for the purpose of this
# problem, we shall assume that a number is Lychrel until proven otherwise. 
# In addition you are given that for every number below ten-thousand, it will 
# either (i) become a palindrome in less than fifty iterations, or, (ii) no one, 
# with all the computing power that exists, has managed so far to map it to a 
# palindrome. In fact, 10677 is the first number to be shown to require over fifty 
# iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?

from time import time
stime = time()
#import Functions # pylint: disable=import-error

def run(lim):
    lychrel_cnt = 0
    for cnt in range(10,lim+1): 
        if rec_lychrel(cnt,0) == True: lychrel_cnt += 1
    return lychrel_cnt

def rec_lychrel(num,cnt):
    cnt+=1
    if cnt > 50: return True
    pal = num + int(str(num)[::-1])
    if pal == int(str(pal)[::-1]): return False
    if rec_lychrel(pal,cnt) == False: return False
    else: return True


print(run(10000))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 249 
# Solve time: 71.96ms 2019.08.05

