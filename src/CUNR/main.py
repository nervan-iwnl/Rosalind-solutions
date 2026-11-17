def solve() -> None:
    with open("src/CUNR/input.txt", "r", encoding="utf-8") as f:
        data = int(f.read().strip())

    result = data
    MOD = 1_000_000
    ans = 1
    
    for n in range(3, data):
        ans = ans * (2*n - 3) % MOD
        
    with open("src/CUNR/output.txt", "w", encoding="utf-8") as f:
        f.write(str(ans))


if __name__ == "__main__":
    solve()
