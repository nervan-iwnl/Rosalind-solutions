with open('./src/TRIE/input.txt') as f:
    DNA = [line.strip() for line in f]
    
trie = {1: {}}
ans = []
for dna in DNA:
    state = 1
    for symb in dna:
        if symb not in trie[state].keys():
            trie[state][symb] = len(trie) + 1
            trie[len(trie) + 1] = {}
            ans.append((state, len(trie), symb))
        state = trie[state][symb]

with open('./src/TRIE/output.txt', 'w') as f:
    for u, v, symb in ans:
        f.write(f'{u} {v} {symb}\n')