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
    dna1, dna2 = read_fasta("src/EDIT/input.txt")
    n = len(dna1)
    m = len(dna2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
        
    for j in range(m + 1):
        dp[0][j] = j
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + (dna1[i - 1] != dna2[j - 1])
            )
            
    with open("src/EDIT/output.txt", "w", encoding="utf-8") as f:
        f.write(str(dp[-1][-1]))


if __name__ == "__main__":
    solve()
