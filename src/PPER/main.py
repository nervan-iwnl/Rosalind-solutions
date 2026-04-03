MOD = 10 ** 6

with open('./src/PPER/input.txt') as f:
    n, k = [int(i) for i in f.read().split()]    

ans = 1

while k > 0:
    ans *= n
    ans %= MOD
    n -= 1
    k -= 1

    
with open('./src/PPER/output.txt', 'w') as f:
    f.write(f'{ans}')