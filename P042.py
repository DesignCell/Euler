# Problem 042
# Coded triangle numbers

# The nth term of the sequence of triangle numbers is given by,
# tn = ½n(n+1); so the first ten triangle numbers are:
#   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding
# to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?

from time import time
stime = time()
#import Functions # pylint: disable=import-error
import string


def triangle(value):
    tri_num = -.5 + (0.25 + 2 * value)**.5 
    if tri_num.is_integer() == True : return True
    return

# save file to list
file_path = r'Python\ProjectEuler\Completed\p042_words.txt' #Path relative to working folder _Programming
words = open(file_path, 'r')
word_list = words.read()
words.close

# clean up list: split by ',' and remove quotes, then sort
word_list = word_list.replace('"','')
word_list = word_list.split(',')
#word_list.sort() # Not required

cnt_triangle = 0
for seq in word_list:
    word_value = 0
    for letter in seq:
        word_value += string.ascii_letters.index(letter.lower()) + 1
    if triangle(word_value) == True: cnt_triangle += 1

print(cnt_triangle)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 162
# Solve time: 14.0ms 09-20-18
