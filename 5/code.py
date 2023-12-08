with open('./5/input.txt', 'r') as f:
    input = [a.strip() for a in f if a.strip() != '']

seeds = [int(a) for a in input[0].split(': ')[1].split(' ')]
maps, map, mapsRev = list(), list(), list()
for a in input[2:]:
    if not str.isalpha(a[0]):
        map.append([int(b) for b in a.split(' ')])
    else :
        maps.append(map)
        map = list()
maps.append(map)
mapsRev = maps.copy()
mapsRev.reverse()

def applyMap(map, s) :
    for m in map :
        if s in range(m[1],m[1]+m[2]) : return m[0] + s-m[1]
    return s

def applyInvMap(map, s) :
    for m in map :
        if s in range(m[0],m[0]+m[2]) : return m[1] + s-m[1]
    return s

def testThread(s) :
    out = s
    for m in mapsRev :
        out = applyMap(m, out)
    
    inRange = [s for s in seeds if s[0]<= out and s[1] >= s[1]]
    return len(inRange) >0

seedOutputs = list()
for s in seeds:
    out = s 
    for m in maps :
        out = applyMap(m, out)
    seedOutputs.append(out)

print(f'Part A: min output = {min(seedOutputs)}') #test assert = 35

seedRanges = [[seeds[i*2], seeds[i*2] + seeds[i*2+1] - 1] for i in range(int(len(seeds)/2))]
print(seedRanges)

for m in maps:
#    print("new map")
    sr2 = list()
    for s in seedRanges : 
        rangeHit = False
        for mR in m :
            if s[0] <= mR[1] + mR[2]-1 and s[1] >= mR[1] : #slice range
                if s[0] < mR[1] : 
                    sr2.append([s[0], mR[1]-1]) # add pre-range
                sr2.append([mR[0] + max(0, s[0] - mR[1]), mR[0] + min(mR[2]-1, s[1] - mR[1])])
                
                if s[1] > mR[1]+mR[2] : 
                    sr2.append([mR[1]+mR[2], s[1]]) #add post-range
                rangeHit = True
        if not rangeHit : sr2.append(s)

    seedRanges = sr2
#    print(seedRanges)

#soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46.

print(f'Part B: min output = {min([r[0] for r in seedRanges])}') #test assert = 46



