import requests
import re 


with open('./src/MPRT/input.txt', 'r') as f:
    proteins = [i.strip() for i in f.readlines()]


with open('./src/MPRT/output.txt', 'w') as f:
    for protein in proteins:
        id = protein.split('_', 1)[0]
        link = f'http://www.uniprot.org/uniprot/{id}.fasta'
        seq = ''.join(requests.get(link).text.splitlines()[1:])
        regex = re.compile("(?=N[^P][ST][^P])")
        matches = regex.finditer(seq) 
        idxs = [str(i.start() + 1) for i in matches]
        if len(idxs) > 0:
            f.write(f'{protein}\n{' '.join(idxs)}\n')