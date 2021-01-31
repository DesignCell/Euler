# Problem 060
# Cyclical figurate numbers

# Find the sum of the only ordered set of six cyclic 4-digit numbers
# for which each polygonal type: triangle, square, pentagonal, hexagonal,
# heptagonal, and octagonal, is represented by a different number in the set.

from time import time
stime = time()
#import Functions # pylint: disable=import-error

#Triangle Returns 4 Digit:      45 - 140
def tri(num):
    return int(num*(num+1)/2)
#Square Returns 4 Digit:        32 - 99
def sq(num):
    return num**2
#Pentagonal Returns 4 Digit:    26 - 81
def pent(num):
    return int(num*(3*num-1)/2)
#Hexagonal Returns 4 Digit:     23 - 70
def hex(num):
    return num*(2*num-1)
#Heptagonal Returns 4 Digit:    21 - 63
def hep(num):
    return int(num*(5*num-3)/2)
#Octagonal Returns 4 Digit:     19 - 58
def oct(num):
    return num*(3*num-2)

#Only to produce limits for each to solve only 4 digit numbers.
def search_digit():
    cnt = 0
    while True:
        cnt+=1
        num = tri(cnt)
        length = len(str(num)) #Run Each Method
        if length == 4: print(cnt,num)
        elif length > 4: return

def search_polys():
    set_of_sets = set()
    set_tri = set()
    for cnt in range(45,141): 
        set_tri.add(tri(cnt))
    set_sq = set()
    for cnt in range(32,100): 
        set_sq.add(sq(cnt))
    set_pent = set()
    for cnt in range(26,82): 
        set_pent.add(pent(cnt))
    set_hex = set()
    for cnt in range(23,71): 
        set_hex.add(hex(cnt))
    set_hep = set()
    for cnt in range(21,64): 
        set_hep.add(hep(cnt))
    set_oct = set()
    for cnt in range(19,59): 
        set_oct.add(oct(cnt))    
    
    
    from itertools import permutations

    num_list = [0,1,2,3,4,5] #,6,7,8,9]
    perm_test_batch = permutations(num_list,6)

    # I feel the real solution is to work from the poly set with the
    # fewest entries to start them permutations of the remaining 5 sets

    #print(len(set_tri),len(set_sq),len(set_pent),len(set_hex),len(set_hep),len(set_oct))
    
    set_of_sets |= set_tri
    set_of_sets |= set_sq
    set_of_sets |= set_pent
    set_of_sets |= set_hex
    set_of_sets |= set_hep
    #set_of_sets |= set_oct

    #This is fucking nonsense...
    # End of if statements produces the following sequence:
    # AABB BBCC CCDD DDEE EEFF FFAA
    for seq_1 in set_oct:
        for seq_2 in set_of_sets:
            if str(seq_1)[2:] == str(seq_2)[0:2]: 
                for seq_3 in set_of_sets:
                    if str(seq_2)[2:] == str(seq_3)[0:2]: 
                        for seq_4 in set_of_sets:
                            if str(seq_3)[2:] == str(seq_4)[0:2]: 
                                for seq_5 in set_of_sets:
                                    if str(seq_4)[2:] == str(seq_5)[0:2]: 
                                        for seq_6 in set_of_sets:
                                            if str(seq_5)[2:] == str(seq_6)[0:2]:
                                                if str(seq_6)[2:] == str(seq_1)[0:2]:
                                                    seq_list = [seq_1,seq_2,seq_3,seq_4,seq_5,seq_6]
                                                    #Test this sequence for the deliverable
                                                    for perm_test_list in perm_test_batch:
                                                        if seq_list[perm_test_list[0]] in set_tri:
                                                            if seq_list[perm_test_list[1]] in set_sq:
                                                                if seq_list[perm_test_list[2]] in set_pent:
                                                                    if seq_list[perm_test_list[3]] in set_hex:
                                                                        if seq_list[perm_test_list[4]] in set_hep:
                                                                            if seq_list[perm_test_list[5]] in set_oct:
                                                                                print(seq_list)
                                                                                return seq_1 + seq_2 + seq_3 + seq_4 + seq_5 + seq_6
                                                    
                                                    seq_list.clear()
                                                        


print(search_polys())

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 28684
# Solve time: 11.99ms 2019.09.19