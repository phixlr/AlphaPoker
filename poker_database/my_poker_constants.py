if __name__ == '__main__':
    import pdb

suits = ['h','d','s','c']
ranks = ['2','3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
hands_by_value
pairs_by_value = []
#hand = list
# pdb.set_trace()
# print(ranks.pop(0))
# print(ranks)
# pdb.set_trace()

for rank in ranks:
    ranks_popped = ranks.copy()
    # pdb.set_trace()
    hand = [0,0,0,0,0]
    # pairvalue = ranks_popped.pop(ranks.index(rank))
    hand[0] = ranks_popped.pop(ranks.index(rank))
    # hand.append(pairvalue) #NB - 'pop' is inplace and returns the popped value
    # pdb.set_trace()
    hand[1] = hand[0]
    # hand.append(pairvalue)
    hand[2] = min(ranks_popped)
    # hand.append(card3)
    ranks_popped.remove(hand[2])
    hand[3] = min(ranks_popped)
    # hand.append(card4)
    ranks_popped.remove(hand[3])
    hand[4] = min(ranks_popped)
    # hand.append(min(ranks_popped))

    pairs_by_value.append(''.join(hand))

print(pairs_by_value)
# pdb.set_trace()

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