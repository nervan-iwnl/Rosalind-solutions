def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


DNA = read_fasta('./src/CONS/input.txt')    

ans = {'A': [0] * len(DNA[0]), 'C': [0] * len(DNA[0]), 'G': [0] * len(DNA[0]), 'T': [0] * len(DNA[0])}

for idx in range(len(DNA[0])):
    for dna in DNA:
        ans[dna[idx]][idx] += 1
        
        
with open('./src/CONS/output.txt', 'w') as f:
    ans_str = ''
    for i in range(len(ans['A'])):
        ans_str += max(ans.keys(), key=lambda base: ans[base][i])
    f.write(f'{ans_str}\n')
    for i in ans:
        f.write(f'{i}: {' '.join([str(i) for i in ans[i]])}\n')
    
