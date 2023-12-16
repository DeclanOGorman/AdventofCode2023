with open('./15/input.txt', 'r') as f:
    input = [a.strip().split(',') for a in f][0]

def hash(inp) :
    curr = 0 
    for a in list(inp) : curr = ((curr + ord(a))*17) % 256
    return curr

def splitLabel(lbl) :
    if '-' in lbl : return lbl[0:-1], '-', 0
    else: return lbl.split("=")[0], '=', int(lbl.split("=")[1])

print(f'Part A: hashed values = {sum([hash(a) for a in input])}') #test assert = 1320

hmap = dict()
for a in input: 
    label, op, focus = splitLabel(a)
    box = hash(label)
    if op == '-' : 
        if box in hmap and label in hmap[box]:
            hmap[box].pop(label)
    else :
        if box not in hmap : hmap[box] = {label:focus}
        else : hmap[box][label] = focus

lenses = [(b+1) * (l+1) * hmap[b][list(hmap[b].keys())[l]] for b in hmap for l in range(len(hmap[b]))]
print(f'Part B: hashmap value = {sum(lenses)}') #test assert = 145