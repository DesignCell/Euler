# Problem 14
# Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:

#		n → n/2 (n is even)
#		n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
#		13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

from time import time
stime = time()

tried = {}  # Creat Dictionary
cnt, num, mcnt, mstart = 0, 0, 0, 0
lim = 1000000

for start in range(1, lim):
	num = start  #Set string number
	cnt = 0
	while num != 1:
		if num in tried.keys():
			cnt += tried[num]
			num = 1
			if cnt > mcnt:  #Record Max Count and Max Start#
				mcnt = cnt
				mstart = start
			continue
		if num % 2 == 0:
			num = num / 2
		else:
			num = 3 * num + 1
		cnt += 1  # Add step in sequnce

		if cnt > mcnt:  #Record Max Count and Max Start#
			mcnt = cnt
			mstart = start
	tried[start] = cnt

print(mstart, '	', mcnt)

print('Finished: Time ', ((time() - stime) * 1000), 'ms')

# Solution	: 837799
# Solve time: 15975.74ms 04-25-18
