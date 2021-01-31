# Problem 9
# Special Pythagorean Triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from time import time
start = time()

def search():
	for cnt1 in range(1,999):
		for cnt2 in range(cnt1+1,1000):
			for cnt3 in range(cnt2+2, 1001):
				if (cnt1+cnt2+cnt3)==1000:
					if (cnt1**2+cnt2**2)==cnt3**2:
						print(cnt1,',',cnt2,',',cnt3)
						#print(cnt1*cnt2*cnt3)
						return cnt1*cnt2*cnt3
#search()
print(search())

print('Finished: Time ', ((time()-start)*1000),'ms')

# 13  Adjacent Product = 31875000
# Solve time 32526.5ms 04-17-18