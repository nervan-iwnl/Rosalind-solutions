MOD = 10 ** 6

with open('./src/SSET/input.txt') as f:
    n = int(f.read())
    
    
with open('./src/SSET/output.txt', 'w') as f:
    f.write(f'{pow(2, n, MOD)}')