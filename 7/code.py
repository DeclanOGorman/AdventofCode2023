with open('./7/test.txt', 'r') as f:
    hands = [[list(a.strip().split(" ")[0]),int(a.strip().split(" ")[1])] for a in f]

def handType(a) :
    cards = dict([(c, a.count(c)) for c in set(a)]) 
    if len(cards) == 1 : #five of a kind
        return 7
    elif [1 for c in cards if cards[c] == 4]: # four of a kind
        return 6
    elif len(cards) == 2: # full house
        return 5
    elif len(cards) == 3 and : # 3 of a kind
        return 4
    else :
        return 0

print(handType(list('KAAKK')))
#def winningHand(a,b) :
#    if () :    

#print(hands)
#Five of a kind, where all five cards have the same label: AAAAA
#Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#High card, where all cards' labels are distinct: 23456