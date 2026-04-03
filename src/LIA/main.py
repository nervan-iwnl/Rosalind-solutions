import math


with open("./src/LIA/input.txt") as f:
    k, n = map(int, f.readline().split())


ans = 0

total = 2 ** k
p = 0.25

for i in range(n, total + 1):
    ans += math.comb(total, i) * (p ** i) * ((1 - p) ** (total - i))
    

with open("./src/LIA/output.txt", "w") as f:
    f.write(f"{ans:.6f}")