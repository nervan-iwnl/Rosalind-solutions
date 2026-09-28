

def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs[0]


def solve() -> None:
    data = read_fasta('src/CAT/input.txt')
    n = len(data)
    dp = [[0] * n for _ in range(n)]
    pairs = ['AU', 'UA', 'CG', 'GC']
    
    for length in range(2, n + 1, 2):
        for l in range(n - length + 1):
            r = length + l - 1
            for k in range(l + 1, r + 1, 2):
                if data[k] + data[l] not in pairs: continue
                inside = 1 if k == l + 1 else dp[l + 1][k - 1]
                after = 1 if k == r else dp[k + 1][r]
                dp[l][r] += inside * after
                dp[l][r] %= 1_000_000
                
    result = dp[0][n - 1]

    with open("src/CAT/output.txt", "w", encoding="utf-8") as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
