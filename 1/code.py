with open('./1/input.txt', 'r') as f:
    input = [a.strip() for a in f]

nums = [int(i[0]+i[-1]) for i in [[i for i in a if str.isdigit(i)] for a in input]]
print(f'Part A: sum of calibration = {sum(nums)}') #test assert = 142

# retain start and end chars to solve for overlapping numbers in the sequence
numMap = {"one" : "o1e", "two" : "t2o", "three" : "t3e", "four" : "f4r", "five": "f5e", "six" : "s6x", "seven" : "s7n", "eight" : "e8t", "nine" : "n9e"}
for n in numMap: input = [str.replace(i, n, numMap[n]) for i in input]
nums = [int(i[0]+i[-1]) for i in [[i for i in a if str.isdigit(i)] for a in input]]

print(f'Part B: sum of calibration = {sum(nums)}') #test assert = 281