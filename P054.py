# Problem 054
# Poker Hands

# hand ranked: 0-9
# card valued: 02-14, dictionary mapping card to value
# 02,03,04,05,06,07,08,09,10, J, Q, K, A
# 02,03,04,05,06,07,08,09,10,11,12,13,14
# combine rank & value into three digit number for total value comparison
# Total value range: 002-914
# Stack 1st, 2nd, 3rd level value to compar hand valve

from time import time
stime = time()
#import Functions # pylint: disable=import-error

# game_list[0-999 games][0-1 player hands][0-4 cards]
def extract_file():
    # save file to list
    import os
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    file_name = "P054_poker.txt"
    file_path = os.path.join(script_dir, file_name)
    extracted = open(file_path, 'r')
    extracted_list = extracted.read().replace(' ','').split('\n')
    extracted.close

    game_list = []
    for cnt_game in range(0,len(extracted_list)): 
        ply1_hand = []
        ply2_hand = []
        for cnt_hand in range(0,10,2): 
            ply1_hand.append(str(extracted_list[cnt_game])[cnt_hand:cnt_hand+2])
            ply2_hand.append(str(extracted_list[cnt_game])[10+cnt_hand:10+cnt_hand+2])
        hands = [ply1_hand,ply2_hand]
        game_list.append(hands)
    return game_list #[0-999 games][0-1 player hands][0-4 cards]

# Run
def run():
    game_list = extract_file()
    ply1_cnt = 0
    for game in game_list: #loops through games
        ply1 = search_value(game[0])
        ply2 = search_value(game[1])
        if ply1 > ply2: ply1_cnt += 1
    return ply1_cnt

# Determine Card Value
def search_value(hand):
    f_bit = flush(hand)
    s_bit = straight(hand)

    #Card value dictionary
    card_dict = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}

    #9 & 8, 814000 = Royal Flush
    if f_bit == True and s_bit != False: return 800000 + card_dict[s_bit] * 1000
    
    #7 Four of a kind
    four_bit = four_of_a_kind(hand)
    if four_bit != False: return 700000 + card_dict[four_bit] * 1000

    #6 Full House
    full_bit = full_house(hand)
    if full_bit != False: return 600000 + card_dict[full_bit] * 1000

    #5 Flush
    #4 Straight
    if s_bit != False: return 400000 + card_dict[s_bit] * 1000

    #3 Three of a kind
    three_bit = three_of_a_kind(hand)
    if three_bit != False:
        if f_bit != False: return 500000 + 300 + card_dict[three_bit]
        return 300000 + card_dict[three_bit] * 1000
    
    #2 Two Pair
    two_bit = two_pair(hand)
    if two_bit != False:
        if f_bit != False: return 500000 + 200 + card_dict[two_bit[0]] + card_dict[two_bit[1]] / 100
        return 200000 + card_dict[two_bit[0]] * 1000 + 200 + card_dict[two_bit[1]]

    #1 One Pair
    one_bit = one_pair(hand)
    if one_bit != False:
        if f_bit != False: return 500000 + 100 + card_dict[one_bit]
        value = 100000 + card_dict[one_bit] * 1000 
        card_dict.pop(one_bit)
        value += high(hand,card_dict)
        return value
    
    #0 High Card
    if f_bit != False: return 500000 + high(hand,card_dict)
    return high(hand,card_dict)

#7 Four of a kind: Four cards of the same value, returns false or true card
def four_of_a_kind(hand):
    card_list = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    for card in card_list:
        if kind(hand,card) == 4: return card
    return False

#6 Full House: Three of a kind and a pair.
def full_house(hand):
    card_list = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    cnt = 0
    three = ''
    for card in card_list:
        card_cnt = kind(hand,card)
        if card_cnt < 2: continue
        if card_cnt == 2: cnt += 2
        if card_cnt ==3: 
            cnt +=3
            three = card
    if cnt != 5: return False
    return three

#5 Flush: All card of the same suit
def flush(hand):
    for card in hand:   
        if str(card)[-1] != str(hand[0])[-1]: return False
    return True

#4 Straight: All cards are consecutive values, returns false or true card
def straight(hand):
    consecutive = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    cnt = 0
    for con in consecutive:
        flag = False
        for card in hand: 
            if card[0] == con: 
                if cnt == 4: return con
                flag = True
        if flag ==True:
            cnt += 1
        else: 
            cnt =0
    return False

#3 Three of a Kind: Three cards of the same value
def three_of_a_kind(hand):
    card_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    for card in card_list:
        if kind(hand,card) == 3: return card
    return False

#2 Two Pair: Two different pairs
def two_pair(hand):
    card_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    flag = 0
    for card in card_list:
        if kind(hand,card) == 2:
            if flag != 0: return flag, card
            flag = card
    return False

#1 One Pair: Two cards of the same value
def one_pair(hand):
    card_list = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    for card in card_list:
        if kind(hand,card) == 2: return card   
    return False

#0 High Card: Highest value card
def high(hand,card_dict):
    value = 0
    for card in hand:
        if card[0] not in card_dict: continue
        card_value = card_dict[card[0]]
        if card_value > value: value = card_value
    return value

# Search list in hand list: returns True/False
def search_card(hand,search):
    for card_s in search:
        flag = False
        for card_h in hand:
            if card_h[0] == card_s: flag = True
        if flag == False: return False
    return True

# Kind: returns # of card from sigle 
def kind(hand,card):
    cnt = 0
    for kind in hand:
        if str(kind)[0] == card: cnt+=1
    return cnt

# Testing...Testing...123?
def test_sample():
    #game 1
    hand = ['5H','5C','6S','7S','KD'] # 105000
    hand = ['2C','3S','8S','8D','TD'] # 108000 Ply2
    #game 2
    hand = ['5D','8C','9S','JS','AC'] # 000014 ply1
    hand = ['2C','5C','7D','8S','QH'] # 000012
    #game 3
    hand = ['2D','9C','AS','AH','AC'] # 314000 
    hand = ['3D','6D','7D','TD','QD'] # 500012 ply2
    #game 4
    hand = ['4D','6S','9H','QH','QC'] # 112009 ply1
    hand = ['3D','6D','7H','QD','QS'] # 112007
    #game 5
    hand = ['2H','2D','4C','4D','4S'] # 604000 ply1
    hand = ['3C','3D','3S','9S','9D'] # 603000
    
    print(search_value(hand))

# Run
print(run())

print('Solve Time: ', round(((time() - stime) * 1000), 2), 'ms')

# Solution	: 376
# Solve time: 286.07 ms 2019.08.04

