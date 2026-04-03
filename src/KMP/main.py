def read_fasta(filename):
    with open(filename) as f:
        sequences = []
        current_seq = None
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                sequences.append("") 
            else:
                sequences[-1] += line
    return sequences


DNA = read_fasta('./src/KMP/input.txt')[0]


def prefix_function(s):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


pi = prefix_function(DNA)

with open('./src/KMP/output.txt', 'w') as f:
    f.write(' '.join(map(str, pi)))