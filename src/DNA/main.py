with open('./src/DNA/input.txt', 'r') as file:
    sequence = file.read()
    
print(sequence.count('A'), sequence.count('C'), sequence.count('G'), sequence.count('T'))