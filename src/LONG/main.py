def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


def overlap(str1, str2):
    for i in range(len(str1), len(str1) // 2, -1):
        if str1[-i:] == str2[:i]:
            return i
    return 0


reads = read_fasta('./src/LONG/input.txt')
reads = [r for r in reads if not any(r != s and r in s for s in reads)]
nxt, prev, ov = {}, {}, {}

for i, a in enumerate(reads):
    for j, b in enumerate(reads):
        if j != i:
            k = overlap(reads[i], reads[j])
            if k:
                nxt[i], prev[j], ov[(i, j)] = j, i, k
                
i = next(i for i in range(len(reads)) if i not in prev)
ans = reads[i]
while i in nxt:
    j = nxt[i]
    ans += reads[j][ov[(i, j)]:]
    i = j

with open('./src/LONG/output.txt', 'w') as f:
    f.write(ans)
    
