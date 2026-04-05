def solve() -> None:
    with open("src/EVAL/input.txt", "r", encoding="utf-8") as f:
        n = int(f.readline())
        DNA = f.readline().strip()
        arr = [float(i) for i in f.readline().strip().split()]
    
    result = []
    for gc_cnt in arr:
        ans = (n - len(DNA) + 1)
        for chr in DNA:
            if chr in 'GC':
                ans *= gc_cnt / 2 
            else:
                ans *= (1 - gc_cnt) / 2
        result.append(str(ans))
    with open("src/EVAL/output.txt", "w", encoding="utf-8") as f:
        f.write(' '.join(result))


if __name__ == "__main__":
    solve()
