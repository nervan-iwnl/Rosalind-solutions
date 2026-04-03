with open('./src/INOD/input.txt') as f:
    n = int(f.read())

with open('./src/INOD/output.txt', 'w') as f:
    f.write(f'{n - 2}')