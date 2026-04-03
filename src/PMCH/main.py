from math import factorial

def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


DNA = read_fasta('./src/PMCH/input.txt')[0]

with open('./src/PMCH/output.txt', 'w') as f:
    f.write(f'{factorial(DNA.count('A')) * factorial(DNA.count('C'))}')
    
