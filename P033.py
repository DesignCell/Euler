# Problem 033
# Digit cancelling fractions

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting
# to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in
# value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from time import time
stime = time()
#import Functions # pylint: disable=import-error
import fractions
prod_num = 1
prod_dem = 1
 
for den10s in range(1,10):
    for den1s in range(0,10):
        num_den = den10s * 10 + den1s
        for num10s in range(1,10):
            for num1s in range(0,10):
                num_num = num10s * 10 + num1s
                if num_num >= num_den: continue
                if num1s == num10s and den1s == den10s: continue
                if den10s != 0 and den1s != 0: 
                    if num1s == den1s and (num10s / den10s) == (num_num / num_den):    
                        prod_num *= num_num
                        prod_dem *= num_den
                        print(num_num,num_den,num10s,den10s)
                        continue
                    if num10s == den1s and (num1s  / den10s) == (num_num / num_den):  
                        prod_num *= num_num
                        prod_dem *= num_den  
                        print(num_num,num_den,num1s ,den10s)
                        continue
                if den1s != 0: 
                    if num1s == den10s and (num10s / den1s ) == (num_num / num_den):    
                        prod_num *= num_num
                        prod_dem *= num_den
                        print(num_num,num_den,num10s, den1s)
                        continue
                    if num10s == den10s and (num1s  / den1s ) == (num_num / num_den):   
                        prod_num *= num_num
                        prod_dem *= num_den
                        print(num_num,num_den,num1s,  den1s)
                        continue

print(prod_dem/prod_num)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 100
# Solve time: 10.99ms 06-27-18