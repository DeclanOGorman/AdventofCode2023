with open('./14/input.txt', 'r') as f:
    input = [list(a.strip()) for a in f]

def dropRocks(field) :
    for y in range(len(field)) :
        for x in range(len(field[0])) : 
            if field[y][x] == 'O' :
                y2 = y-1 
                while y2 >= 0 and field[y2][x] == '.' : y2 -= 1
                field[y][x] = '.'
                field[y2+1][x] = 'O'

def loadSum(field) :
    return sum([len(field)-y for x in range(len(field[0])) 
            for y in range(len(field)) if field[y][x] == 'O'])

dropRocks(input)
print(f'Part A: sum of north load = {loadSum(input)}') #test assert = 136

history, field, spins, loads = list(), input, 0, list()
while str(field) not in history : #and spins == 0
    spins += 1
    history.append(str(field))
    for i in range(4) :
        dropRocks(field)
        field = list(map(list, zip(*field)))#[::-1]
        field = [a[::-1] for a in field]
    loads.append(loadSum(field))

loopStart = history.index(str(field))
loopLen = (len(history)) - history.index(str(field))
loopTarget = 1000000000
print(f'Part B: load after 1bn = {loads[((loopTarget-loopStart) % loopLen) + loopStart-1]}') #test assert = 64