from functools import cache
import sys
sys.setrecursionlimit(2000)

@cache
def f(l, r):
    if r - l <= 1:
        return 1
    
    ans = f(l + 1, r)
    for k in range(l + 1, r):
        if (s[l], s[k]) in {("A", "U"), ("U", "A"),
                            ("C", "G"), ("G", "C")}:
            ans += f(l + 1, k) * f(k + 1, r)

    return ans % 1_000_000

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
    global s
    s = read_fasta("src/MOTZ/input.txt")
    result = f(0, len(s))

    with open("src/MOTZ/output.txt", "w", encoding="utf-8") as file:
        file.write(str(result))


if __name__ == "__main__":
    solve()
