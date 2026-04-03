with open('./src/IEV/input.txt', 'r') as f:
    k = list(map(int, f.readline().split()))
    
with open('./src/IEV/output.txt', 'w') as f:
    f.write(str(2 * (1 * k[0] + 1 * k[1] + 1 * k[2] + 0.75 * k[3] + 0.5 * k[4])) + '\n')
    
    