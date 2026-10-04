def build_de_brujin_graph(arr):
    ans = set()
    complement = str.maketrans("ACGT", "TGCA")
    for el in arr:
        ans.add((el[:-1], el[1:]))
        rev = el.translate(complement)[::-1]
        ans.add((rev[:-1], rev[1:]))
    return ans


def solve() -> None:
    with open("src/DBRU/input.txt", "r", encoding="utf-8") as f:
        data = f.read().split()

    result = build_de_brujin_graph(data)
    print(result)

    with open("src/DBRU/output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(f"({a}, {b})" for a, b in sorted(result)))


if __name__ == "__main__":
    solve()
