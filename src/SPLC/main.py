def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


dna_seq = read_fasta('./src/SPLC/input.txt')

rna = dna_seq[0]

for intron in dna_seq[1:]:
    rna = rna.replace(intron, '')
    
    
rna = rna.replace('T', 'U')

CODON = {
    "UUU":"F","UUC":"F","UUA":"L","UUG":"L",
    "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
    "UAU":"Y","UAC":"Y","UAA":"Stop","UAG":"Stop",
    "UGU":"C","UGC":"C","UGA":"Stop","UGG":"W",

    "CUU":"L","CUC":"L","CUA":"L","CUG":"L",
    "CCU":"P","CCC":"P","CCA":"P","CCG":"P",
    "CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "CGU":"R","CGC":"R","CGA":"R","CGG":"R",

    "AUU":"I","AUC":"I","AUA":"I","AUG":"M",
    "ACU":"T","ACC":"T","ACA":"T","ACG":"T",
    "AAU":"N","AAC":"N","AAA":"K","AAG":"K",
    "AGU":"S","AGC":"S","AGA":"R","AGG":"R",

    "GUU":"V","GUC":"V","GUA":"V","GUG":"V",
    "GCU":"A","GCC":"A","GCA":"A","GCG":"A",
    "GAU":"D","GAC":"D","GAA":"E","GAG":"E",
    "GGU":"G","GGC":"G","GGA":"G","GGG":"G",
}

ans = ''
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]    
    if CODON[codon] == "Stop":
        break
    ans += CODON[codon]

with open('./src/SPLC/output.txt', 'w') as file:
    file.write(ans)