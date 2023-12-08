with open('./7/input.txt', 'r') as f:
    hands = [[list(a.strip().split(" ")[0]),int(a.strip().split(" ")[1])] for a in f]

def convertHandsInt(h) :
    return [10 if i == 'T' else 11 if i == 'J' else 12 if i == 'Q' else 13 if i =='K' else 14 if i == 'A' else int(i) for i in h]

def handType(a) :
    cards = dict([(c, a.count(c)) for c in set(a)]) 
    if len(cards) == 1 : #five of a kind
        return 7
    elif [1 for c in cards if cards[c] == 4]: # four of a kind
        return 6
    elif len(cards) == 2: # full house
        return 5
    elif len([1 for c in cards if cards[c] == 3]) > 0 : # 3 of a kind
        return 4
    elif len([1 for c in cards if cards[c] == 2]) == 2 : # 2 pair
        return 3
    elif len([1 for c in cards if cards[c] == 2]) == 1 : # 1 pair
        return 2
    else :
        return 1

def highestCard(a,b) : #1 if a wins, -1 if b wins
    for i in range(len(a)) :
        if a[i] > b[i] : return 1
        elif a[i] < b[i] : return -1
    return 0

def cardScore(a) : 
    return sum([a[i] * (14**(len(a) -i-1)) for i in range(len(a))])

for h in hands:
    h[0] = convertHandsInt(h[0])

print(handType(list('A231K')))
print(highestCard(convertHandsInt(list('QKQ10')), convertHandsInt(list('QAQ42'))))

def compareHands(a,b) :
    if handType(a) > handType(b) : return 1
    elif handType(a) > handType(b) : return -1
    else : return (highestCard(a,b))

def handKey(a) :
    return handType(a[0])*(14**5) + cardScore(a[0])

print(hands)
hands.sort(key = handKey, reverse = False)
for h in hands : print(f"{handType(h[0])} {(14**5)}, {cardScore(h[0])} - {[h[0][i] * (14**(len(h[0]) -i)) for i in range(len(h[0]))]}")
print(hands)

score = sum([(i+1) * hands[i][1] for i in range(len(hands))])
print(f'Part A: sum of ordered hands = {score}') #test assert = 6440