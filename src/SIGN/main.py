from itertools import permutations, product

with open('./src/SIGN/input.txt') as f:
    n = int(f.readline())


def signed_permutations(n):
    perms = []
    for perm in permutations(range(1, n + 1)):
        for signs in product([1, -1], repeat=n):
            perms.append(' '.join(f'{sign * num}' for sign, num in zip(signs, perm)))
    return perms


with open('./src/SIGN/output.txt', 'w') as f:
    f.write(f'{len(signed_permutations(n))}\n')
    f.write('\n'.join(signed_permutations(n)))