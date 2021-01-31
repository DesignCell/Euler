def factorial(number): #Returns Factorial of single argument
    if number <= 1: return 1 #Base Case 0! & 1! = 1
    else:   return number * factorial(number - 1)

def factor_sum(num): #Returns Proper Facotr Sum
    sfact = set()
    sfact.add(1) #add (1) as starting factor not tested to eliminate input number return
    for cnt in range(2, int(num**0.5)+1):
        if num%cnt == 0:
            sfact.add(cnt)
            if num/cnt != cnt: 
                sfact.add(num/cnt)
    return sum(sfact)

def is_prime(num): #returns True if argument Prime, else False
    if num <= 1:
        return False
    for cntp in range(2, (int((num**.5)))+1):
        if num % cntp == 0:
            return False
    return True

def primes_sieve(limit): 
    #Returns list of primes up to including argument
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

def primes_sieve_range(lim_bot,lim_top): 
    #Returns list of primes between bottom and top argument
    primes = dict()
    for i in range(2,lim_top): primes[i] = True
    limitn = len(primes)+1

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True and i > lim_bot]

def consecutive_primes(num_a,num_b): # Returns consecutive prime count
    cnt = 0
    prime = True
    while prime == True:
        quad = cnt**2 + num_a * cnt + num_b
        prime = is_prime(abs(quad))
        if prime == True:  cnt+=1 #Includes Zero
    return cnt

def palindrome(num): # Returns True if input int/str is palindromic
    num = str(num)
    if num == num[::-1]: return True
    return False

def pent_check(value):
    pent_num = (1 + (1 + 24 * value)**.5 ) / 6
    if pent_num.is_integer() == True:   return True
    return False

def tri_check(value): # Not used since all Hex numbers are Tri
    tri_num = -.5 + (0.25 + 2 * value)**.5 
    if tri_num.is_integer() == True:    return True
    return

def hex_check(value): # Not used since directly solving Hex numbers in searchHex
    hex_num = (1 + (1 + 8 * value)**.5 ) /4
    if hex_num.is_integer() == True:    return True
    return

def are_Permutation(num1,num2):
    str1 = sorted(str(num1))
    str2 = sorted(str(num2))

    for cnt in range(len(str1)):
        if str1[cnt] != str2[cnt]: return False
    return True