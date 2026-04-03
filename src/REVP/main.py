def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


DNA = read_fasta('./src/REVP/input.txt')[0]

swap = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

ans = []

for i in range(len(DNA) - 3):
    for k in range(4, 13):
        if i + k > len(DNA):
            break
        curr = DNA[i:i + k]
        swap_curr = ''.join([swap[c] for c in reversed(curr)])
        if curr == swap_curr:
            print(curr)
            ans.append([i + 1, k])
            
with open('./src/REVP/output.txt', 'w') as f:
    for a, b in ans:
        f.write(f'{a} {b}\n')
