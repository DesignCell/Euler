# Problem 062
# Cubic Permutations

# The cube, 41063625 (345**3), can be permuted to produce two other cubes:
# 56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube
# which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.


from time import time
stime = time()
#import Functions # pylint: disable=import-error

def cube(lim_min,lim_max):
    #compile cube list within range limits
    num_list = []
    for num in range(lim_min,lim_max):
        num_list.append(num**3)

    #Test list for permutations
    for seq in num_list:
        perm_cnt = 0
        for sub_seq in num_list:
            if sub_seq <= seq: continue #Limit sequnce to greater numbers in list
            if arePermutation(seq,sub_seq) == True: 
                perm_cnt += 1
                #print(perm_cnt,seq,sub_seq)
            if perm_cnt == 4: return seq
    return False

#Permutation Test, assumes same length, returns true/false
def arePermutation(num1,num2):
    str1 = sorted(str(num1))
    str2 = sorted(str(num2))

    for cnt in range(len(str1)):
        if str1[cnt] != str2[cnt]: return False
    return True

print(cube(4642,10000)) # Examples 345, 384, 405


print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 127035954683
# Solve time: 3349.42ms 2019.09.14


"""
Solution:
127035954683
352045367981
373559126408
569310543872
589323567104

Num ** 3 = Digit Length
Search Reanges
01 1
02 3
03 5
04 10
05 22
06 47
07 100
08 216
09 465
10 1000
11 2155
12 4642
13 10000
14 21545
15 46416
16 100000
17 215444
18 464159
19 1000000
20 2154435
21 4641589
22 10000000
23 21544347
24 46415889
25 100000000
Solve Time:  51204.87 ms
"""