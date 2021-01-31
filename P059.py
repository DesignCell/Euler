# Problem 059
# XOR decryption

# ASCII # > chr() > Key Value
# (3) lower case character
# Must contain 'common english words'

# Decrypt the message and find the sum of the ASCII values in the original text.

# https://radiusofcircle.blogspot.com/2016/06/problem-59-project-euler-solution-with-python.html
# https://www.mathblog.dk/project-euler-59-xor-encryption/

from time import time
stime = time()
#import Functions # pylint: disable=import-error

from collections import Counter

# game_list[0-999 games][0-1 player hands][0-4 cards]
def extract_file():
    #File Path relative to current run directory. Opens adjacent
    import os
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    file_name = "P059_cipher.txt"
    file_path = os.path.join(script_dir, file_name)
    extracted = open(file_path, 'r')
    extracted_list = extracted.read().split(",")
    extracted.close
    extracted_list = list(map(int,extracted_list)) # Needed?
 
    return extracted_list

def decrypt(): # Search each batch for most common " " = 32
    message = extract_file()
    bin_1 = Counter(message[0::3]).most_common(1)  #69
    bin_2 = Counter(message[1::3]).most_common(1)  #88
    bin_3 = Counter(message[2::3]).most_common(1)  #80
    keys = [bin_1[0][0]^32,bin_2[0][0]^32,bin_3[0][0]^32]

    key_cnt = 0
    decrypted = []
    message_decrypted = []
    for seq in message:
        decrypted.append(seq ^ keys[key_cnt])
        key_cnt += 1
        if key_cnt == 3: key_cnt = 0

    for seq_write in decrypted:
        message_decrypted.append(chr(seq_write))

    message_sum = 0
    for seq_sum in decrypted: 
        #print(seq_sum)
        message_sum += seq_sum
    print(message_sum)
    #return message_sum
    seperator = ', '
    return seperator.join(message_decrypted)

print(decrypt())


print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 129448
# Solve time: 6.0ms 2019.08.20

