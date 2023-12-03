with open('./3/input.txt', 'r') as f:
    input = [list(a.strip()) for a in f]

def isSymbol(s) : return not str.isdigit(s) and not s == "."

def isAdjacentToSymbol(grid, xS, yS) :
    for x in range(max(xS-1,0), min(xS+2,len(grid[0]))) :
        for y in range(max(yS-1,0), min(yS+2,len(grid))) :
            if isSymbol(grid[y][x]) : return True
    return False

def hashGear(x, y) : return y*len(input) + x

def adjacentGear(grid, xS, yS) :
    gears = set()
    for x in range(max(xS-1,0), min(xS+2,len(grid[0]))) :
        for y in range(max(yS-1,0), min(yS+2,len(grid))) :
            if grid[y][x] == "*" : gears.add(hashGear(x,y))
    return gears

parts = list()
num = ""
isPart = False
gears = set()
gearsD = dict()
for y in range(len(input)) :
    for x in range(len(input[0])) :
        if str.isdigit(input[y][x]) :
            num += input[y][x]
            if isAdjacentToSymbol(input, x, y) : isPart = True
            g = adjacentGear(input, x, y)
            if len(g) > 0 and g not in gears : 
                gears = gears.union(adjacentGear(input, x, y))
        else :
            if isPart : 
                parts.append(int(num))
                for g in gears :
                    if g in gearsD.keys() :
                        gearsD[g].append(int(num))
                    else :
                        gearsD[g] = [int(num)]
            num = ""
            isPart = False
            gears = set()
    if isPart : 
        parts.append(int(num))
        for g in gears :
            if g in gearsD.keys() :
                gearsD[g].append(int(num))
            else :
                gearsD[g] = [int(num)]
    num = ""
    isPart = False
    gears = set()

print(f'Part A: sum of part nums = {sum(parts)}') #test assert = 4361

sumGears = sum([gearsD[g][0]*gearsD[g][1] for g in gearsD if len(gearsD[g]) == 2])
print(f'Part A: sum of part nums = {sumGears}') #test assert = 467835