from itertools import permutations
from math import factorial

with open('./src/PERM/input.txt') as f:
    n = int(f.readline())
    


perms = permutations(range(1, n + 1))

with open('./src/PERM/output.txt', 'w') as f:
    f.write(str(factorial(n)) + '\n')
    for perm in perms:
        f.write(' '.join(map(str, perm)) + '\n')
        
