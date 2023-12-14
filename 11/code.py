with open('./11/input.txt', 'r') as f:
    input = [list(a.strip()) for a in f] 

def getExpansions(starMap) :
    emptyRows, emptyCols = list(),list()
    i, j = 0, 0
    while i < len(starMap) : # code assumes map is square
        if '#' not in starMap[i] :
            emptyRows.append(i)
        if '#' not in [a[i] for a in starMap] :
            emptyCols.append(i)
        i += 1

    return emptyRows, emptyCols

def expand(a, b, nums, expand) :
    return len([n for n in nums if a < n < b or b < n < a]) * (expand-1)

def getStarDists(stars, cols, rows, dist) :
    starDist = dict()
    for s1 in stars :
        for s2 in stars :
            if s1 != s2 and (s2,s1) not in starDist:
                starDist[(s1,s2)] = abs(s1[0]-s2[0])+expand(s1[0], s2[0],cols,dist)
                starDist[(s1,s2)] += abs(s1[1]-s2[1])+expand(s1[1], s2[1],rows,dist)

    return starDist

emptyRows, emptyCols = getExpansions(input)
stars = [(x,y) for y in range(len(input)) for x in range(len(input[0])) if input[y][x] == '#']

starDist = getStarDists(stars, emptyCols, emptyRows, 2)
print(f'Part A: distance between stars = {sum(starDist.values())}') #test assert = 374

starDist = getStarDists(stars, emptyCols, emptyRows, 1000000)
print(f'Part B: distance between stars @1m = {sum(starDist.values())}')