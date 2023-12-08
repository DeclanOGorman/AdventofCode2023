import numpy as np

with open('./8/input.txt', 'r') as f:
    ins = f.readline().strip()
    mapRaw = [a.strip().replace(' ','').replace('=(',',').replace(')','').split(',') for a in f if a.strip() != ""]

loc, target, steps, map = 'AAA', 'ZZZ', 0, dict([(a[0], [a[1], a[2]]) for a in mapRaw])
while loc != target :
    loc = map[loc][0 if ins[steps % len(ins)] =='L' else 1]
    steps += 1

print(f'Part A: steps to get to {target} = {steps}') #test assert = 2
loc, steps, step1, stepN = {a for a in map if a.endswith('A')}, 0, list(), list()

for s in loc :
    steps, cLoc, first = 0, s, True
    while not cLoc.endswith('Z') :
        cLoc = map[cLoc][0 if ins[steps % len(ins)] =='L' else 1]
        steps += 1
        if cLoc.endswith('Z') : 
            step1.append(steps)

for s in range(len(step1) -1) :
    c = g = max(step1[s],step1[s+1])
    while c%step1[s] !=0 or c%step1[s+1] !=0 :
        c += g
    step1[s+1] = c

print(f'Part B: steps to get to simultaneous targets = {step1[-1]}') #test assert = 6