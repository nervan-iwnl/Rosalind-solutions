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
    with open("src/SCSP/input.txt", 'r') as f:
        s, t = f.readlines()
        s = s.strip()
        t = t.strip()
        
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = ''
    i = len(s)
    j = len(t)
    while i > 0 and j > 0: 
        if s[i - 1] == t[j - 1]:
            result = s[i - 1] + result
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
            result = s[i] + result
        else:
            j -= 1 
            result = t[j] + result
    
    while i > 0:
        result = s[i - 1] + result
        i -= 1
        
    while j > 0:
        result = t[j - 1] + result
        j -= 1
    
    with open("src/SCSP/output.txt", "w", encoding="utf-8") as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
