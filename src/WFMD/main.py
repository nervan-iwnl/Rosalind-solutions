from math import comb


def solve() -> None:
    with open("src/WFMD/input.txt", "r", encoding="utf-8") as f:
        N, m, g, k  = map(int, f.read().split())

    dp = [[0] * (2 * N + 1)]
    dp[0][2 * N -  m] = 1.0
    
    for generation in range(g):
        dp.append([0.0] * (2 * N + 1))
        for i in range(2 * N + 1):
            p = i / (2 * N)
            for j in range(2 * N + 1):
                Tij = comb(2 * N, j) * p ** j * (1 - p) ** (2 * N - j)
                dp[-1][j] += dp[-2][i] * Tij
    
    result = sum(dp[-1][k:])

    with open("src/WFMD/output.txt", "w", encoding="utf-8") as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
