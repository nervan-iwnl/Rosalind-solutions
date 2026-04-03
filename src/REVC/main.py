dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

with open('./src/REVC/input.txt', 'r') as file:
    sequence = file.read()
    
rev_comp = ''.join(dic[base] for base in reversed(sequence))
print(rev_comp)