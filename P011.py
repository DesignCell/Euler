# Problem 11
# Largest product in a grid

# In the 20×20 grid below, four numbers along a diagonal line have (not) been marked in red.

from time import time
start = time()

matrix =[
	[ 8, 2,22,97,38,15,00,40,00,75, 4, 5, 7,78,52,12,50,77,91, 8], #  1
	[49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62,00], #  2
	[81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65], #  3
	[52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91], #  4
	[22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80], #  5
	[24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50], #  6
	[32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70], #  7
	[67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21], #  8
	[24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72], #  9
	[21,36,23, 9,75,00,76,44,20,45,35,14,00,61,33,97,34,31,33,95], # 10
	[78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92], # 11
	[16,39, 5,42,96,35,31,47,55,58,88,24,00,17,54,24,36,29,85,57], # 12
	[86,56,00,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58], # 13
	[19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40], # 14
	[ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66], # 15
	[88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69], # 16
	[ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36], # 17
	[20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16], # 18
	[20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54], # 19
	[ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48]  # 20
	]#1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?

mprod =0

#Search Product Left-Right
for cnt1y in range(0,20):
	for cnt1x in range(0,17): #20-4
		tprod = matrix[cnt1y][cnt1x]*matrix[cnt1y][cnt1x+1]*matrix[cnt1y][cnt1x+2]*matrix[cnt1y][cnt1x+3]
		if tprod > mprod:	mprod = tprod
		
#Search Product Up-Down
for cnt1y in range(0,17):
	for cnt1x in range(0,20): #20-4
		tprod = matrix[cnt1y][cnt1x]*matrix[cnt1y+1][cnt1x]*matrix[cnt1y+2][cnt1x]*matrix[cnt1y+3][cnt1x]
		if tprod > mprod:	mprod = tprod
		
#Search Product UpLeft-DownRight
for cnt1y in range(0,17):
	for cnt1x in range(0,17): #20-4
		tprod = matrix[cnt1y][cnt1x]*matrix[cnt1y+1][cnt1x+1]*matrix[cnt1y+2][cnt1x+2]*matrix[cnt1y+3][cnt1x+3]
		if tprod > mprod:	mprod = tprod

#Search Product DownLeft-UpRight
for cnt1y in range(0,17):
	for cnt1x in range(0,17): #20-4
		tprod = matrix[cnt1y+3][cnt1x]*matrix[cnt1y+2][cnt1x+1]*matrix[cnt1y+1][cnt1x+2]*matrix[cnt1y][cnt1x+3]
		if tprod > mprod:	mprod = tprod
		
print(mprod)

print('Finished: Time ', ((time()-start)*1000),'ms')

# Solution	: 70600674
# Solve time: 1.59ms 04-19-28










