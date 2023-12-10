from matplotlib.path import Path

with open('./10/input.txt', 'r') as f:
    input = [list(a.strip()) for a in f]

N, E, S, W = (0,-1), (1,0), (0,1), (-1,0) #x,y
pipes = {"|" : [N,S], "-" : [E,W], "L" : [N,E], "S" : [],
         "J" : [N,W], "7" : [S,W], "F" : [S,E], "." : []}

def getStartOptions(s) :
    opts = list()
    for y in range(-1,2) :
        for x in range(-1,2) :
            if s[0]+x < 0 or s[1]+y < 0 or (x,y) == (0,0) or s[0]+x >= len(input[0]) or s[1]+y >= len(input) or input[s[1]+y][s[0]+x] == '.': continue
            for p in pipes[input[s[1]+y][s[0]+x]] :
                if p[0] == x * -1 and p[1] == y * -1 : opts.append(((s[0]+x,s[1]+y),1))
    return opts

start = [(b,a) for a in range(len(input)) for b in range(len(input[0])) if input[a][b] == 'S'][0] #x,y
c, finished, path, queue = start, False, {start : 0}, getStartOptions(start)

for q in queue : path[q[0]] = 1
while len(queue) > 0 : 
    c, steps = queue.pop()    
    for d in pipes[input[c[1]][c[0]]] :
        test = c[0]+d[0], c[1]+d[1]
        if (test) not in path or path[test] > steps+1:
            path[test] = steps+1
            queue.append((test, steps+1))

print(f'Part A: furthest point in loop = {max(path.values())}') #test assert = 8

# The matplotlib was a reddit nudge after failing to do a flood fill (having not read the question properly on encased points and spent too long on the previous solution)...

plot = Path(list(path.keys()))
outside = [1 for y in range(len(input)) for x in range(len(input[0])) if not (x, y) in path and plot.contains_point((x, y))]

print(f'Part B: furthest point in loop = {len(outside)}') #test assert = 8