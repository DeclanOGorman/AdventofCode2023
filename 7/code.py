with open('./7/input.txt', 'r') as f:
    hands = [[list(a.strip().split(" ")[0]),int(a.strip().split(" ")[1])] for a in f]

def convertHandsInt(h) :
    return [10 if i == 'T' else 11 if i == 'J' else 12 if i == 'Q' else 13 if i =='K' else 14 if i == 'A' else int(i) for i in h]

def handType(a) :
    cards = dict([(c, a.count(c)) for c in set(a) if c != 1]) 
    numJokers = a.count(1)
    if len(cards) <= 1 : #five of a kind
        return 7
    elif len([1 for c in cards if cards[c] == 4-numJokers]) > 0: # four of a kind
        return 6
    elif len(cards) == 2: # full house
        return 5
    elif len([1 for c in cards if cards[c] == 3 - numJokers]) > 0 : # 3 of a kind
        return 4
    elif len([1 for c in cards if cards[c] == 2]) == 2 : # 2 pair
        return 3
    elif len([1 for c in cards if cards[c] == 2 - numJokers]) : # 1 pair
        return 2
    else :
        return 1

def cardScore(a) : 
    return sum([a[i] * (14**(len(a) -i-1)) for i in range(len(a))])

def handKey(a) :
    return handType(a[0])*(14**5) + cardScore(a[0])

for h in hands:
    h[0] = convertHandsInt(h[0])
    
hands.sort(key = handKey)
score = sum([(i+1) * hands[i][1] for i in range(len(hands))])

print(f'Part A: sum of ordered hands = {score}') #test assert = 6440

for h in hands : h[0] = [1 if c == 11 else c for c in h[0]] #reset Joker score
hands.sort(key = handKey)
score = sum([(i+1) * hands[i][1] for i in range(len(hands))])

print(f'Part B: sum of ordered hands with jokers = {score}') #test assert = 5905