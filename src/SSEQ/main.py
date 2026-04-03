def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


DNA, motif = read_fasta('./src/SSEQ/input.txt')


ans = []
l: int = 0
for i, el in enumerate(DNA):
    if motif[l] == el:
        ans.append(str(i + 1))
        l += 1

    if len(ans) >= len(motif):
        break 
        
with open('./src/SSEQ/output.txt', 'w') as f:
    f.write(' '.join(ans))