def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


dna1, dna2 = read_fasta('./src/TRAN/input.txt')


transitions = 0
transversions = 0
for i in range(len(dna1)):
    if dna1[i] != dna2[i]:
        if (dna1[i] in 'AG' and dna2[i] in 'AG') or (dna1[i] in 'CT' and dna2[i] in 'CT'):
            transitions += 1
        else:
            transversions += 1


with open('./src/TRAN/output.txt', 'w') as f:
    f.write(f'{transitions / transversions}\n')