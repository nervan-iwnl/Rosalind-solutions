with open('./src/RNA/input.txt', 'r') as file:
    sequence = file.read()

print(sequence.replace('T', 'U'))