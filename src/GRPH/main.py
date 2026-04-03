def read_fasta(path):
    seqs, cur = [], []
    names = []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
            names.append(line.strip()[1:])
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs, names


DNA, names = read_fasta('./src/GRPH/input.txt')


graph = {}

for i in range(len(DNA)):
    pref = DNA[i][:3]
    graph.setdefault(pref, []).append(i)
        

with open('./src/GRPH/output.txt', 'w') as f:
    for i, dna in enumerate(DNA):
        if dna[-3:] not in graph:
            continue
        for prefix in graph[dna[-3:]]:
            if names[i] != names[prefix]:
                f.write(f'{names[i]} {names[prefix]}\n')
