def solve() -> None:
    with open("src/AFRQ/input.txt", "r", encoding="utf-8") as f:
        data = [float(token) for token in f.read().split()]    
    result = []
    for q in data:
        result.append(str(1 - (1 - (q)**0.5)**2))

    with open("src/AFRQ/output.txt", "w", encoding="utf-8") as f:
        f.write(' '.join(result))


if __name__ == "__main__":
    solve()
