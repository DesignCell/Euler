# Problem 15
# Lattice Paths

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

from time import time
stime = time()

xy = 21  #Verties of grid: Grid + 1

# list comprehension
grid = [[0 for x in range(xy)] for y in range(xy)] 

for y in range(0, xy):
	for x in range(0, xy):
		if x == 0 or y == 0:
			#set 0,0 to 1 for starting position
			grid[y][x] =1
		else:
			#Add one up & Add one left
			grid[y][x] = grid[y-1][x] + grid[y][x-1]

#print bottom right sum
print(str(grid[20][20]))

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 137846528820
# Solve time: 0.29ms
