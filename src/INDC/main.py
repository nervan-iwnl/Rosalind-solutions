from math import log10, comb

def solve() -> None:
    with open("src/INDC/input.txt", "r", encoding="utf-8") as f:
        n = int(f.read())
        
    ans = []
    combs = 0
    for k in range(2 * n, 0, -1):
        tmp = comb(2 * n, k) / 2**(2 * n)
        combs += tmp
        ans.append(f"{log10(combs):.4f}")
        
    ans.reverse()
    with open("src/INDC/output.txt", "w", encoding="utf-8") as f:
        f.write(' '.join(ans))


if __name__ == "__main__":
    solve()
