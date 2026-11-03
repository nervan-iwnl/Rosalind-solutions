def solve() -> None:
    with open("src/SEXL/input.txt", "r", encoding="utf-8") as f:
        data = [float(token) for token in f.read().split()]    
    
    result = []
    for q in data:
        result.append(str(2 * q * (1 - q)))

    with open("src/SEXL/output.txt", "w", encoding="utf-8") as f:
        f.write(" ".join(result))


if __name__ == "__main__":
    solve()
