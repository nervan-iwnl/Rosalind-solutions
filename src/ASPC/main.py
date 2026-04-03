with open('./src/ASPC/input.txt') as f:
    n, m = [int(i) for i in f.readline().split()]

fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i

ans = 0
for k in range(m, n + 1):
    ans += fact[n] // (fact[k] * fact[n - k])
    ans %= 1_000_000
    
with open('./src/ASPC/output.txt', 'w') as f:
    f.write(f'{ans}')