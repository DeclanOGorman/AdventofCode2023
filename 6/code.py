with open('./6/test.txt', 'r') as f:
    times = [int(a) for a in f.readline().strip().split(": ")[1].split(" ") if a != '']
    distance = [int(a) for a in f.readline().strip().split(": ")[1].split(" ") if a != '']

def raceDist(hold, time) :
    return (hold, (time-hold) * (hold)) 

raceSum = 1
for i in range(len(times)) :
    winningDists = [raceDist(t, times[i]) for t in range(1, times[i]) if raceDist(t, times[i])[1] > distance[i]]
    raceSum *= max(1, len(winningDists))

print(f'Part A: product of winning race choices = {raceSum}') #test assert = 288

timeB = int(''.join([str(a) for a in times]))
distanceB = int(''.join([str(a) for a in distance]))

minWin, maxWin, won = 0,timeB,False
while not won :
    minWin += 1
    won = raceDist(minWin,timeB)[1] > distanceB

won = False
while not won :
    maxWin -= 1
    won = raceDist(maxWin,timeB)[1] > distanceB

print(f'Part B: # of winning races = {minWin}, {maxWin} = {maxWin - minWin + 1}') #test assert = 71503