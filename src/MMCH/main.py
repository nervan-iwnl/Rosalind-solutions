from math import perm

def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


DNA = read_fasta('./src/MMCH/input.txt')[0]

with open('./src/MMCH/output.txt', 'w') as f:
    a_count = DNA.count('A')
    u_count = DNA.count('U')
    c_count = DNA.count('C')
    g_count = DNA.count('G')
    f.write(f'{perm(max(a_count, u_count), min(a_count, u_count)) * perm(max(g_count, c_count), min(g_count, c_count))}')
    
