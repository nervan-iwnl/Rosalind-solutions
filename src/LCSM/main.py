def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


DNAs = read_fasta('./src/LCSM/input.txt')

ans = ''


for r in range(len(DNAs[0])):
    for l in range(r):
        substr = DNAs[0][l:r]
        is_true: bool = True
        for string in DNAs:
            if substr not in string:
                is_true = False
                break 
        if is_true and len(substr) > len(ans): ans = substr

with open('./src/LCSM/output.txt', 'w') as f:
    f.write(ans)