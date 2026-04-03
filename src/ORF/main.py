def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


DNA = read_fasta('./src/ORF/input.txt')[0]
swap = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
DNA_swap = ''.join([swap[c] for c in reversed(DNA)])

DNA_strings = [DNA, DNA[1:], DNA[2:], DNA_swap, DNA_swap[1:], DNA_swap[2:]]
ans = set()

CODON = {
    "TTT":"F","TTC":"F","TTA":"L","TTG":"L",
    "TCT":"S","TCC":"S","TCA":"S","TCG":"S",
    "TAT":"Y","TAC":"Y","TAA":"Stop","TAG":"Stop",
    "TGT":"C","TGC":"C","TGA":"Stop","TGG":"W",

    "CTT":"L","CTC":"L","CTA":"L","CTG":"L",
    "CCT":"P","CCC":"P","CCA":"P","CCG":"P",
    "CAT":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "CGT":"R","CGC":"R","CGA":"R","CGG":"R",

    "ATT":"I","ATC":"I","ATA":"I","ATG":"M",
    "ACT":"T","ACC":"T","ACA":"T","ACG":"T",
    "AAT":"N","AAC":"N","AAA":"K","AAG":"K",
    "AGT":"S","AGC":"S","AGA":"R","AGG":"R",

    "GTT":"V","GTC":"V","GTA":"V","GTG":"V",
    "GCT":"A","GCC":"A","GCA":"A","GCG":"A",
    "GAT":"D","GAC":"D","GAA":"E","GAG":"E",
    "GGT":"G","GGC":"G","GGA":"G","GGG":"G",
}

for DNA in DNA_strings:
    for i in range(len(DNA) - 2):
        if DNA[i:i + 3] == 'ATG':
            protein = ''
            for j in range(i, len(DNA) - 2, 3):
                codon = DNA[j:j + 3]
                if CODON[codon] == 'Stop':
                    ans.add(protein)
                    break
                else:
                    protein += CODON[codon]
                    
with open('./src/ORF/output.txt', 'w') as f:
    for a in ans:
        f.write(f'{a}\n')           
