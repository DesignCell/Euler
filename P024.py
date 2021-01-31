from time import time
stime = time()

# Problem 24
# Lexicographic permutations

# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the 
# digits 1, 2, 3 and 4. If all of the permutations are listed
# numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:

#   012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

limit = 1000000
count = 0

while count <= limit:
    for cnt0 in range (0,10):
        for cnt1 in range (0,10):
            if cnt1 == cnt0: continue
            for cnt2 in range (0,10):
                if cnt2 == cnt0: continue
                if cnt2 == cnt1: continue
                for cnt3 in range (0,10):
                    if cnt3 == cnt0: continue
                    if cnt3 == cnt1: continue
                    if cnt3 == cnt2: continue
                    for cnt4 in range (0,10):
                        if cnt4 == cnt0: continue
                        if cnt4 == cnt1: continue
                        if cnt4 == cnt2: continue
                        if cnt4 == cnt3: continue
                        for cnt5 in range (0,10):
                            if cnt5 == cnt0: continue
                            if cnt5 == cnt1: continue
                            if cnt5 == cnt2: continue
                            if cnt5 == cnt3: continue
                            if cnt5 == cnt4: continue
                            for cnt6 in range (0,10):
                                if cnt6 == cnt0: continue
                                if cnt6 == cnt1: continue
                                if cnt6 == cnt2: continue
                                if cnt6 == cnt3: continue
                                if cnt6 == cnt4: continue
                                if cnt6 == cnt5: continue
                                for cnt7 in range (0,10):
                                    if cnt7 == cnt0: continue
                                    if cnt7 == cnt1: continue
                                    if cnt7 == cnt2: continue
                                    if cnt7 == cnt3: continue
                                    if cnt7 == cnt4: continue
                                    if cnt7 == cnt5: continue
                                    if cnt7 == cnt6: continue
                                    for cnt8 in range (0,10):
                                        if cnt8 == cnt0: continue
                                        if cnt8 == cnt1: continue
                                        if cnt8 == cnt2: continue
                                        if cnt8 == cnt3: continue
                                        if cnt8 == cnt4: continue
                                        if cnt8 == cnt5: continue
                                        if cnt8 == cnt6: continue
                                        if cnt8 == cnt7: continue
                                        for cnt9 in range (0,10):
                                            if cnt9 == cnt0: continue
                                            if cnt9 == cnt1: continue
                                            if cnt9 == cnt2: continue
                                            if cnt9 == cnt3: continue
                                            if cnt9 == cnt4: continue
                                            if cnt9 == cnt5: continue
                                            if cnt9 == cnt6: continue
                                            if cnt9 == cnt7: continue
                                            if cnt9 == cnt8: continue
                                            count += 1
                                            if count == limit: print(cnt0,cnt1,cnt2,cnt3,cnt4,cnt5,cnt6,cnt7,cnt8,cnt9)

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 2783915460
# Solve time: 49771.67ms 05-19-18