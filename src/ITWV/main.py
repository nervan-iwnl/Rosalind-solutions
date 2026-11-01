def check(piece, t, u):
    dp = [[False] * (len(u) + 1) for _ in range(len(t) + 1)]
    dp[0][0] = True

    for i in range(len(t) + 1):
        for j in range(len(u) + 1):
            if not dp[i][j]:
                continue

            pos = i + j

            if i < len(t) and piece[pos] == t[i]:
                dp[i + 1][j] = True

            if j < len(u) and piece[pos] == u[j]:
                dp[i][j + 1] = True

    return dp[len(t)][len(u)]


def search(s, t, u):
    length = len(t) + len(u)

    for start in range(len(s) - length + 1):
        if check(s[start:start + length], t, u):
            return 1

    return 0


def solve() -> None:
    with open("src/ITWV/input.txt", "r", encoding="utf-8") as f:
        dna = f.readline().strip()
        parts = [i.strip() for i in f.readlines()]

    ans = [['0' for _ in range(len(parts))] for _ in range(len(parts))]
    for i in range(len(parts)):
        for j in range(len(parts)):
            if search(dna, parts[i], parts[j]):
                ans[i][j] = '1'
    with open("src/ITWV/output.txt", "w", encoding="utf-8") as f:
        for string in ans:
            f.write(' '.join(string))
            f.write('\n')


if __name__ == "__main__":
    solve()
