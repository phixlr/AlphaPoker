if __name__ == '__main__':
    import pdb

suits = ['h','d','s','c']
ranks = ['2','3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

pack_of_cards = ['2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Ah',
                 '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Ad',
                 '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Ac',
                 '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'As']

ranks_as_integers = {'2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
hands_by_value = []
high_card_by_value = []
pairs_by_value = []
two_pairs_by_value = []
trips_by_value = []
straights_by_value = []
flushes_by_value = []
full_Hise_by_value = []
fours_by_value = []
straight_flushes_by_value=[]

hand = ['0','0','0','0','0']

ranks_popped = ranks.copy()

def return_hand_as_integers(cards_as_string):
    temphand = []
    handlength = len(cards_as_string)
    for i in range(handlength):
        temphand.append(ranks_as_integers.get(cards_as_string[i]))
    temphand.sort()
    # if temphand == [2,3,4,5,14]:   THESE TWO LINEA WORKED
    #     temphand = [1,2,3,4,5]
    if 2 in temphand and 3 in temphand and 4 in temphand and 5 in temphand and 14 in temphand:
        temphand.pop()
        temphand.append(1)
        temphand.sort()
    return temphand

def return_hand_as_string (cards_as_intlist, sort_hand = True, sort_high_to_low = False, join = True):
    if sort_hand:
        cards_as_intlist.sort()
        if 2 in cards_as_intlist and 3 in cards_as_intlist and 4 in cards_as_intlist and 5 in cards_as_intlist and 14 in cards_as_intlist:
            cards_as_intlist.pop()
            cards_as_intlist.append(1)
            cards_as_intlist.sort()
        if sort_high_to_low:
            cards_as_intlist.reverse()
    temphand = []
    handlength = len(cards_as_intlist)
        # pdb.set_trace()
    for i in range(handlength):
        if 1 < cards_as_intlist[i] < 10:
            temphand.append(str(cards_as_intlist[i]))
        elif cards_as_intlist[i] == 1 or cards_as_intlist[i] == 14:
            temphand.append('A')
        elif cards_as_intlist[i] == 10:
            temphand.append('T')
        elif cards_as_intlist[i] == 11:
            temphand.append('J')
        elif cards_as_intlist[i] == 12:
            temphand.append('Q')
        elif cards_as_intlist[i] == 13:
            temphand.append('K')
    if join:
        return ''.join(temphand)
    else:
        return temphand

def remove_duplicate_hands(handlist, return_as_string = True):
    newcardlist =[]
    for i in handlist:
        newcardlist.append(return_hand_as_integers(i))
    newcardlist.sort()
    j=1
    while j<len(newcardlist):
        if newcardlist[j] == newcardlist[j-1]:
            newcardlist.pop(j)
        else:
            j += 1

    if return_as_string:
        stringslist = []
        for s in newcardlist:
            stringslist.append(return_hand_as_string(s))
        return stringslist
    else:
        return newcardlist

# print(return_hand_as_string([10,3,12,5,14]))

#High card loop:
for card1 in ranks:
    if card1 == 'T':
        break
    hand[0] = card1
    ranks_popped.remove(card1)
    for card2 in ranks_popped:
        ranks_popped2=ranks_popped.copy()
        if card2 != card1:
            hand[1] = card2
            ranks_popped2.remove(card2)
            for card3 in ranks_popped2:
                ranks_popped3 = ranks_popped2.copy()
                if card3 != card2:
                    hand[2] = card3
                    ranks_popped3.remove(card3)
                    for card4 in ranks_popped3:
                        ranks_popped4 = ranks_popped3.copy()
                        if card4 != card3:
                            hand[3] = card4
                            ranks_popped4.remove(card4)
                            for card5 in ranks_popped4:
                                if card5 != card4:
                                    hand[4] = card5
                                    if ranks.index(card5) - ranks.index(card1) < 5:
                                        continue
                                    elif 'A' in hand and '2' in hand and '3' in hand and '4' in hand and '5' in hand:
                                        continue
                                    high_card_by_value.append(''.join(hand))


newlist = remove_duplicate_hands(high_card_by_value)
print(newlist)
print(len(newlist))

# print(return_hand_as_integers('2345A'))
print(return_hand_as_string([2,11,4,5,10]))
# newlist = remove_duplicate_hands(newlist)
#
# print(newlist)
# print(len(newlist))

#Pairs loop:
for card1 in range(len(ranks)):
    ranks_popped = ranks.copy()
    hand[0] = ranks_popped.pop(card1)
    hand[1] = hand[0]
    ranks_popped2 = ranks_popped.copy()
    for card3 in ranks_popped:
        hand[2] = ranks_popped2.pop(0)
        ranks_popped3 = ranks_popped2.copy()
        for card4 in ranks_popped2:
            hand[3] = ranks_popped3.pop(0)
            for card5 in ranks_popped3:
                hand[4] = card5
                pairs_by_value.append(''.join(hand))

# print(pairs_by_value)
# print(len(pairs_by_value))

#Two_Pairs loop:
for card1 in range(len(ranks)):
    ranks_popped = ranks.copy()
    hand[0] = ranks_popped.pop(card1)
    hand[1] = hand[0]
    ranks_popped2 = ranks_popped.copy()
    for card3 in range(len(ranks_popped)):
        ranks_popped2 = ranks_popped.copy()
        hand[2] = ranks_popped2.pop(card3)
        hand[3] = hand[2]
        ranks_popped3 = ranks_popped2.copy()
        for card5 in ranks_popped2:
            hand[4] = card5
            two_pairs_by_value.append(''.join(hand))
                # pairs_by_value.append(''.join(hand))
# pdb.set_trace()
hands_by_value.append(pairs_by_value)

# print(two_pairs_by_value)
# print(len(two_pairs_by_value))

pack_of_cards = ['2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Ah',
                 '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Ad',
                 '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Ac',
                 '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'As']

poker_hands = {"High_Card": ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'],
               "Pair": ['22', '33', '44', '55', '66', '77', '88', '99', 'TT', 'JJ', 'QQ', 'KK', 'AA'],
               "Two_Pairs": ['2233', '33', '44', '55', '66', '77', '88', '99', 'TT', 'JJ', 'QQ', 'KK', 'AA'],
               "Trips": ['222', '333', '444', '555', '666', '777', '888', '999', 'TTT', 'JJJ', 'QQQ', 'KKK', 'AAA'],
               "Straight": ['A2345', '23456', '34567', '45678', '56789', '6789T', '789TJ', '89TJQ', '9TJQK', 'TJQKA'],
               "Flush": ['hhhhh', 'ddddd', 'sssss', 'ccccc'],
               "Full_House": ['22233', '22244', '22255', '22266', '22277', '22288', '22299', '222TT', '222JJ', '222QQ',
                              '222KK', '222AA',
                              '33322', '33344', '33355', '33366', '33377', '33388', '33399', '333TT', '333JJ', '333QQ',
                              '333KK', '333AA',
                              '44422', '44433', '44455', '44466', '44477', '44488', '44499', '444TT', '444JJ', '444QQ',
                              '444KK', '444AA',
                              '55522', '55533', '55544', '55566', '55577', '55588', '55599', '555TT', '555JJ', '555QQ',
                              '555KK', '555AA',
                              '66622', '66633', '66644', '66655', '66677', '66688', '66699', '666TT', '666JJ', '666QQ',
                              '666KK', '666AA',
                              '77722', '77733', '77744', '77755', '77766', '77788', '77799', '777TT', '777JJ', '777QQ',
                              '777KK', '777AA',
                              '88822', '88833', '88844', '88855', '88866', '88877', '88899', '888TT', '888JJ', '888QQ',
                              '888KK', '888AA',
                              '99922', '99933', '99944', '99955', '99966', '99977', '99988', '999TT', '999JJ', '999QQ',
                              '999KK', '999AA',
                              'TTT22', 'TTT33', 'TTT44', 'TTT55', 'TTT66', 'TTT77', 'TTT88', 'TTT99', 'TTTJJ', 'TTTQQ',
                              'TTTKK', 'TTTAA',
                              'JJJ22', 'JJJ33', 'JJJ44', 'JJJ55', 'JJJ66', 'JJJ77', 'JJJ88', 'JJJ99', 'JJJTT', 'JJJQQ',
                              'JJJKK', 'JJJAA',
                              'QQQ22', 'QQQ33', 'QQQ44', 'QQQ55', 'QQQ66', 'QQQ77', 'QQQ88', 'QQQ99', 'QQQTT', 'QQQJJ',
                              'QQQKK', 'QQQAA',
                              'KKK22', 'KKK33', 'KKK44', 'KKK55', 'KKK66', 'KKK77', 'KKK88', 'KKK99', 'KKKTT', 'KKKJJ',
                              'KKKQQ', 'KKKAA',
                              'AAA22', 'AAA33', 'AAA44', 'AAA55', 'AAA66', 'AAA77', 'AAA88', 'AAA99', 'AAATT', 'AAAJJ',
                              'AAAQQ', 'AAAKK'],
               "Four_of_a_kind": ['22223', '22224', '22225', '22226', '22227', '22228', '22229', '2222T', '2222J',
                                  '2222Q', '2222K', '2222A',
                                  '33332', '33334', '33335', '33336', '33337', '33338', '33339', '3333T', '3333J',
                                  '3333Q', '3333K', '3333A',
                                  '44442', '44443', '44445', '44446', '44447', '44448', '44449', '4444T', '4444J',
                                  '4444Q', '4444K', '4444A',
                                  '55552', '55553', '55554', '55556', '55557', '55558', '55559', '5555T', '5555J',
                                  '5555Q', '5555K', '5555A',
                                  '66662', '66663', '66664', '66665', '66667', '66668', '66669', '6666T', '6666J',
                                  '6666Q', '6666K', '6666A',
                                  '77772', '77773', '77774', '77775', '77776', '77778', '77779', '7777T', '7777J',
                                  '7777Q', '7777K', '7777A',
                                  '88882', '88883', '88884', '88885', '88886', '88887', '88889', '8888T', '8888J',
                                  '8888Q', '8888K', '8888A',
                                  '99992', '99993', '99994', '99995', '99996', '99997', '99998', '9999T', '9999J',
                                  '9999Q', '9999K', '9999A',
                                  'TTTT2', 'TTTT3', 'TTTT4', 'TTTT5', 'TTTT6', 'TTTT7', 'TTTT8', 'TTTT9', 'TTTTJ',
                                  'TTTTQ', 'TTTTK', 'TTTTA',
                                  'JJJJ2', 'JJJJ3', 'JJJJ4', 'JJJJ5', 'JJJJ6', 'JJJJ7', 'JJJJ8', 'JJJJ9', 'JJJJT',
                                  'JJJJQ', 'JJJJK', 'JJJJA',
                                  'QQQQ2', 'QQQQ3', 'QQQQ4', 'QQQQ5', 'QQQQ6', 'QQQQ7', 'QQQQ8', 'QQQQ9', 'QQQQT',
                                  'QQQQJ', 'QQQQK', 'QQQQA',
                                  'KKKK2', 'KKKK3', 'KKKK4', 'KKKK5', 'KKKK6', 'KKKK7', 'KKKK8', 'KKKK9', 'KKKKT',
                                  'KKKKJ', 'KKKKQ', 'KKKKA',
                                  'AAAA2', 'AAAA3', 'AAAA4', 'AAAA5', 'AAAA6', 'AAAA7', 'AAAA8', 'AAAA9', 'AAAAT',
                                  'AAAAJ', 'AAAAQ', 'AAAAK'],
               "Straight_Flush": ['Ah2h3h4h5h', '2h3h4h5h6h', '3h4h5h6h7h', '4h5h6h7h8h', '5h6h7h8h9h', '6h7h8h9hTh',
                                  '7h8h9hThJh', '8h9hThJhQh', '9hThJhQhKh', 'ThJhQhKhAh',
                                  'Ad2d3d4d5d', '2d3d4d5d6d', '3d4d5d6d7d', '4d5d6d7d8d', '5d6d7d8d9d', '6d7d8d9dTd',
                                  '7d8d9dTdJd', '8d9dTdJdQd', '9dTdJdQdKd', 'TdJdQdKdAd',
                                  'As2s3s4s5s', '2s3s4s5s6s', '3s4s5s6s7s', '4s5s6s7s8s', '5s6s7s8s9s', '6s7s8s9sTs',
                                  '7s8s9sTsJs', '8s9sTsJsQs', '9sTsJsQsKs', 'TsJsQsKsAs',
                                  'Ac2c3c4c5c', '2c3c4c5c6c', '3c4c5c6c7c', '4c5c6c7c8c', '5c6c7c8c9c', '6c7c8c9cTc',
                                  '7c8c9cTcJc', '8c9cTcJcQc', '9cTcJcQcKc', 'TcJcQcKcAc']
               }
# throughout this module top/bottom refers to a deck face down on the table
POS_TOP = 0
POS_BOTTOM = 1