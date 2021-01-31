from time import time
stime = time()

# Problem 22
# Names Score

# Using names.txt (right click and 'Save Link/Target As...'), a
# 46K text file containing over five-thousand first names, begin
# by sorting it into alphabetical order. Then working out the
# alphabetical value for each name, multiply this value by its
# alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
# name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

# save file to list
file_path = r'Python\ProjectEuler\P022_names.txt' #Path relative to working folder _Programming
names = open(file_path, 'r')
name_list = names.read()
names.close

# clean up list: split by ',' and remove quotes, then sort
name_list = name_list.replace('"','')
name_list = name_list.split(',')
name_list.sort()

# function to determin name score from alpha place sum
def name_score(name,place):
    lscore = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    sum_score = 0
    for seq in range(len(name)):
        sum_score += lscore[name[seq].lower()]
    #print(place, name, sum_score, place * sum_score)
    return sum_score * place
  
total = 0
for seq in range(len(name_list)):
    total += name_score(name_list[seq],seq+1)

print(total)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 871198282
# Solve time: 275.83ms 05-14-18