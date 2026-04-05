def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


def solve() -> None:
    dct = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    dna = read_fasta("src/KMER/input.txt")[0]
    result = [0] * 256

    for idx in range(3, len(dna)):
        res_idx = 0
        for i in range(0, -4, -1):
            res_idx += 4**abs(i) * dct[dna[idx + i]] 
        result[res_idx] += 1

    with open("src/KMER/output.txt", "w", encoding="utf-8") as f:
        f.write(' '.join([str(i) for i in result]))


if __name__ == "__main__":
    solve()
