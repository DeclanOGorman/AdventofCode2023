with open('./13/input.txt', 'r') as f:
    input, map, l = list(), list(), ""
    for l in f.readlines() :
        if l.strip() == "" :
            input.append(map)
            map = []
        else :
            map.append(list(l.strip()))  
    input.append(map)

def findMirror(map, smudge) :
    for i in range(0,len(map)-1) :
        diffs = 0
        for j in range(min(i, len(map)-i-2)+1) :
            diffs += len([k for k in range(len(map[0])) if map[i-j][k] != map[i+j+1][k]])
        if diffs == smudge : return i + 1
    return 0

mirrorsY = [findMirror(m, 0) for m in input]
mirrorsX = [findMirror([list(x) for x in zip(*m)], 0) for m in input]
print(f'Part A: reflections = {sum(mirrorsX) + sum(mirrorsY)*100}') #test assert = 405

mirrorsY = [findMirror(m, 1) for m in input]
mirrorsX = [findMirror([list(x) for x in zip(*m)], 1) for m in input]
print(f'Part A: reflections = {sum(mirrorsX) + sum(mirrorsY)*100}') #test assert = 400