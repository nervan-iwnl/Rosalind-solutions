from itertools import product

with open('./src/LEXF/input.txt') as f:
    alphabet = f.readline().strip().split()
    n = int(f.readline().strip())
    
ans = [''.join(p) for p in product(alphabet, repeat=n)]

with open('./src/LEXF/output.txt', 'w') as f:
    f.write('\n'.join(ans))