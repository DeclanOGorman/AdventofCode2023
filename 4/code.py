import math

with open('./4/input.txt', 'r') as f:
    input = [a.strip().split(': ') for a in f]

input = [[a[0], set(a[1].split('|')[0].split(' ')), set(a[1].split('|')[1].split(' '))] for a in input]
numWins = [[1, len(a[1].intersection([i for i in a[2] if i != '']))] for a in input]
numPoints = [int(math.pow(2,a[1]-1)) for a in numWins if a[1] > 0]

print(f'Part A: sum of tickets = {sum(numPoints)}') #test assert = 13

for i in range(len(numWins)) :
    for w in range(numWins[i][1]) :
        numWins[i+w+1][0] += numWins[i][0]

print(f'Part B: sum of cascaded tickets = {sum([a[0] for a in numWins])}') #test assert = 30