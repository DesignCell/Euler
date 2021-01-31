# Problem 4
# Largest Palindrome Product
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from time import time
start = time()
palpro =999 #Largest 3-digit number
palbot = 0
cnt1 = palpro
cnt2 = palpro
pal =0
pro1 =0
pro2 =0

for cnt1 in range (palpro,palbot,-1):
	for cnt2 in range (cnt1,palbot,-1):
		palt = cnt1*cnt2
		if len(str(palt))==6:
			if str(palt)[0]==str(palt)[5]:
				if str(palt)[1]==str(palt)[4]:
					if str(palt)[2]==str(palt)[3]:
						palbot = cnt2
						if palt > pal:
							pal=palt
							pro1=cnt1
							pro2=cnt2
						

print ('Palindrome from the product of ', str(pro1), ' & ', str(pro2), ' is ', str(pal))			
print('Finished: Time ', ((time()-start)*1000),'ms')

# Largest palindrome made from the product of two 3-digit numbers = 993*913=906609
# Solve time 10.93ms 04-13-18