# Problem 17
# Number Letter Counts

#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

from time import time
stime = time()


def ones(num):
	if num == 0: return ''
	if num == 1: return 'one'
	if num == 2: return 'two'
	if num == 3: return 'three'
	if num == 4: return 'four'
	if num == 5: return 'five'
	if num == 6: return 'six'
	if num == 7: return 'seven'
	if num == 8: return 'eight'
	if num == 9: return 'nine'

def tens(num):
	if num == 0: return ''
	if num == 1: return 'ten'
	if num == 2: return 'twenty'
	if num == 3: return 'thirty'
	if num == 4: return 'forty'
	if num == 5: return 'fifty'
	if num == 6: return 'sixty'
	if num == 7: return 'seventy'
	if num == 8: return 'eighty'
	if num == 9: return 'ninety'
	
def teens(num):
	if num == 1: return 'eleven'
	if num == 2: return 'twelve'
	if num == 3: return 'thirteen'
	if num == 4: return 'fourteen'
	if num == 5: return 'fifteen'
	if num == 6: return 'sixteen'
	if num == 7: return 'seventeen'
	if num == 8: return 'eighteen'
	if num == 9: return 'nineteen'

lim = 1000	#Limit Limit 9999
num_word = ''

for cnt in range(1, lim + 1):
	num_w = ''
	length = len(str(cnt))
	#1000s
	if length >= 4:
		num_w += ones(int(str(cnt)[-4])) + 'thousand'
	#100s
	if length >= 3:
		if int(str(cnt)[-3]) !=0:	num_w += ones(int(str(cnt)[-3])) + 'hundred'
		if int(str(cnt)[-2]) != 0 or int(str(cnt)[-1]) != 0:
			num_w += 'and'
	#10s
	if length >= 2:
		if int(str(cnt)[-2]) == 1 and int(str(cnt)[-1]) == 0:
			num_w += 'ten'
		elif int(str(cnt)[-2]) == 1 and int(str(cnt)[-1]) != 0:
			num_w += teens(int(str(cnt)[-1]))
		else:
			num_w += tens(int(str(cnt)[-2]))
	#1s
	if length >=1:
		if length >=2 and int(str(cnt)[-2]) != 1:
			num_w += ones(int(str(cnt)[-1]))
		elif length == 1:	num_w += ones(int(str(cnt)[-1]))
	num_word += num_w
	#print(cnt, '	', num_w)

print(len(num_word))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 21124
# Solve time: 13.33ms 04-27-18
