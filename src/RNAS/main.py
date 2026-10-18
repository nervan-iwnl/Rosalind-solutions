from functools import cache
import sys
sys.setrecursionlimit(2000)

@cache
def f(l, r):
    if r - l <= 1:
        return 1
    
    ans = f(l + 1, r)
    for k in range(l + 4, r):
        if (s[l], s[k]) in {("A", "U"), ("U", "A"),
                            ("C", "G"), ("G", "C"),
                            ('U', 'G'), ('G', 'U')}:
            ans += f(l + 1, k) * f(k + 1, r)

    return ans

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
    with open("src/RNAS/input.txt") as file:
        s = file.read().strip()

    result = f(0, len(s))

    with open("src/RNAS/output.txt", "w", encoding="utf-8") as file:
        file.write(str(result))


if __name__ == "__main__":
    solve()



