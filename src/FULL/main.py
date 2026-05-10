iso_table = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 
            'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 
            'K': 128.09496,  'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 
            'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 
            'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}


def mass_to_aa(mass, tolerance=0.01):
    for aa, m in iso_table.items():
        if abs(mass - m) < tolerance:
            return aa
    return None


def solve() -> None:
    with open("src/FULL/input.txt", "r", encoding="utf-8") as f:
        seq = [float(i) for i in f.readlines()]

    L = seq[0]
    seq = seq[1:]
    
    n = (len(seq) - 2) // 2
    dp = ['' for _ in range(len(seq))]
    
    for j in range(len(seq)):
        for i in range(j):
            diff = seq[j] - seq[i]
            aa = mass_to_aa(diff)
            
            if aa is not None:
                candidate = dp[i] + aa
                
                if len(candidate) > len(dp[j]):
                    dp[j] = candidate
                    
                    if len(candidate) == n:
                        return candidate
    
    return max(dp, key=len)

if __name__ == "__main__":
    with open("src/FULL/output.txt", "w", encoding="utf-8") as f:
        f.write(str(solve()))

    
