import math

with open('./src/RSTR/input.txt') as f:
    n, x = [float(i) for i in f.readline().split()]
    DNA = f.readline()
    

dct = {'A': (1 - x) / 2, 'T': (1 - x) / 2, 'G': x / 2, 'C': x / 2}

dna_prob = 1 - math.prod([dct[i] for i in DNA])

print(dna_prob)
ans = 1 - dna_prob**n


with open('./src/RSTR/output.txt', 'w') as f:
    f.write(f'{ans}')