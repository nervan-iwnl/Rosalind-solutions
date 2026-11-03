iso_table = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 
            'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 
            'K': 128.09496,  'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 
            'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 
            'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}


def build_mass(protein):
    n = len(protein)
    ans = [0] * (2 * n)
    prefix = suffix = 0

    for i in range(n):
        prefix += round(iso_table[protein[i]] * 100_000)
        suffix += round(iso_table[protein[-i - 1]] * 100_000)
        ans[i] = prefix
        ans[n + i] = suffix

    return ans[:-1]


def solve() -> None:
    with open("src/PRSM/input.txt", "r", encoding="utf-8") as f:
        n = int(f.readline())
        candidates = [f.readline().strip() for _ in range(n)]
        data = [round(float(token) * 100_000) for token in f.read().split()]

    ans = (0, 0)
    for protein in candidates:
        freq = {}
        for mass in build_mass(protein):
            for observed in data:
                shift = mass - observed
                freq[shift] = freq.get(shift, 0) + 1       
        if max(freq.values()) >  ans[1]:
            ans = (protein, max(freq.values()))

    with open("src/PRSM/output.txt", "w", encoding="utf-8") as f:
        f.write(f'{ans[1]}\n{ans[0]}')


if __name__ == "__main__":
    solve()
