def prefix_func(s):
    pi = [0] * len(s)
    for i in range(1, len(s)):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


with open('./src/SUBS/input.txt', 'r') as file:
    genome = file.readline().strip()
    pattern = file.readline().strip()
    arr = prefix_func(pattern + '$' + genome)
    print(' '.join([str(i - 2*len(pattern) + 1) for i in range(len(pattern) + 1, len(arr)) if arr[i] == len(pattern)]))
    