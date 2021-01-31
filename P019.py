from time import time
stime = time()
import datetime

# Problem 19
# Counting Sundays

# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

start_date = datetime.date(1901,1,6)
end_date = datetime.date(2000,12,31)

sum_sun = 0

for year in range (start_date.year,end_date.year+1):
    for month in range(1,13):
        if datetime.date(year,month,1).weekday() == 6:
            sum_sun += 1

print(sum_sun)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 171
# Solve time: 4.36ms 05-14-18