with open('./9/input.txt', 'r') as f:
    input = [[int(b) for b in a.strip().split(" ")] for a in f]

def getDelta(seq) :
    d = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
    return [d] if d.count(0) == len(d) else  getDelta(d) + [d]

def extend(seq) :
    for i in range(1, len(seq)) :
        seq[i].append(seq[i][-1] + seq[i-1][-1])
    return seq

def extendLeft(seq) :
    for i in range(1, len(seq)) :
        seq[i].insert(0, seq[i][0] - seq[i-1][0])
    return seq

endSeqs = [extend(getDelta(a) + [a])[-1][-1] for a in input]
print(f'Part A: sum of predicted values {sum(endSeqs)}') #test assert = 18,28,68 / 114

startSeqs = [extendLeft(getDelta(a) + [a])[-1][0] for a in input]
print(f'Part B: sum of preceeding values {sum(startSeqs)}') #test assert = 5,-3,0 / 2