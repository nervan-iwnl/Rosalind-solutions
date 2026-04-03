with open('./src/IPRB/input.txt', 'r') as f:
    k, m, n = map(int, f.read().split())

total = k + m + n

p_recessive = (
    n * (n - 1) / 2
    + m * n * 0.5
    + m * (m - 1) * 1/8
) / (total * (total - 1) / 2)


print(1 - p_recessive)
