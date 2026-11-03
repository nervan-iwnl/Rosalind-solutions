iso_table = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 
            'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 
            'K': 128.09496,  'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 
            'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 
            'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}

def solve() -> None:
    with open("src/SGRA/input.txt", "r", encoding="utf-8") as f:
        data = sorted(map(float, f.read().split()))

    n = len(data)
    dp = ['' for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if len(dp[j]) + 1 < len(dp[i]):
                continue
            for el, val in iso_table.items():
                if  abs(data[i] - data[j] - val) > 10**-4:
                    continue 
                dp[i] = dp[j] + el
                break
    
    result = max(dp, key=len)
    with open("src/SGRA/output.txt", "w", encoding="utf-8") as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
