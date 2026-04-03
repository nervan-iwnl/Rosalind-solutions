import math

with open('./src/PROB/input.txt') as f:
    dna = f.readline().strip()
    arr = list(map(float, f.readline().strip().split()))
    

ans = []

for prob in arr:
    curr = 1
    for nucl in dna:
        if nucl == 'A' or nucl == 'T':
            curr *= (1 - prob) / 2
        else:
            curr *= prob / 2
    ans.append(curr)
    
with open('./src/PROB/output.txt', 'w') as f:
    f.write(' '.join(map(str, [math.log10(x) for x in ans])))