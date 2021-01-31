# Problem 31
# Coin sums
"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
      1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
      1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

from time import time
stime = time()
#import Functions # pylint: disable=import-error

coins = [1,2,5,10,20,50,100,200]
amt = 200
combinations = [0]*(amt+1)
combinations[0] = 1
for coin in coins:
      for amount in range(amt+1):
            if amount >= coin: 
                  #print(coin,amount)
                  combinations[amount] += combinations[(amount-coin)]

print(combinations[-1])
print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 73682
# Solve time: 1.0ms 06-14-18