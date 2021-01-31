from time import time
stime = time()

# Problem 18
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:

tri_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

tri_nr = tri_str.replace('\n',' ')
tri_list = [int(i) for i in tri_nr.split()]

#Determine input size
size = 0
for cnt in range(1,len(tri_list)):
    size += cnt
    if size == len(tri_list):
        size = cnt
        break
    elif size > len(tri_list):
        print('Range Mismatch')

#Build empty array size x size of zeros
tri_set = [[0 for col in range(size)] for row in range(size)] 
#Sort Sized input into list array
for cnt_row in range(0,size):
    for cnt_col in range(0,cnt_row+1):
        tri_set[cnt_row][cnt_col] = tri_list[0]
        del tri_list[0]

#Sum Path
for cnt_row in range(size-2,-1,-1):
    for cnt_col in range(0,cnt_row + 1):
        if tri_set[cnt_row+1][cnt_col] > tri_set[cnt_row+1][cnt_col+1]:
            tri_set[cnt_row][cnt_col] += tri_set[cnt_row+1][cnt_col]
        else:
            tri_set[cnt_row][cnt_col] += tri_set[cnt_row+1][cnt_col+1]

print(tri_set[0][0])

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 1074
# Solve time: 2.0ms 05-11-18
