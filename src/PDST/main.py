def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


def p_distance(dna1, dna2):
    cnt = 0
    for i in range(len(dna1)):
        if (dna1[i] != dna2[i]):
            cnt += 1
    return cnt / len(dna1)

DNA = read_fasta('./src/PDST/input.txt')

dists = [[0] * len(DNA) for _ in range(len(DNA))]


for i in range(len(DNA)):
    for j in range(len(DNA)):
        dists[i][j] = p_distance(DNA[i], DNA[j])
        
        
with open('./src/PDST/output.txt', 'w') as f:
    for a in dists:
        for j in a:
            f.write(f'{j:6f} ')
        f.write('\n')