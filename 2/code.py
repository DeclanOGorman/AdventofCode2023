import numpy
with open('./2/input.txt', 'r') as f:
    input = [a.strip().split(": ") for a in f]

games = [(int(g[0].split(" ")[1]), g[1].split("; ")) for g in input]
games = [(g[0], [(i.split(" ")[1], int(i.split(" ")[0])) for t in g[1] for i in t.split(", ")]) for g in games]

limits = {"red" : 12, "green" : 13, "blue" : 14}
invalid = set()
for g in games:
    for i in g[1]:
        if i[1] > limits[i[0]] : invalid.add(g[0])

validSum = sum(set([g[0] for g in games]).difference(invalid))
print(f'Part A: sum of valid games = {validSum}') #test assert = 8

values = list()
for g in games:
    uniquePieces = dict()
    for p in g[1] :
        uniquePieces[p[0]] = max(uniquePieces[p[0]] if (p[0] in uniquePieces.keys()) else 0, p[1]) 
    values.append(uniquePieces)

print(f'Part A: sum of unique pieces = {sum([numpy.prod(list(v.values())) for v in values])}') #test assert = 2286
