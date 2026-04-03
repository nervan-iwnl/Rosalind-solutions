with open('./src/HAMM/input.txt', 'r') as file:
    gen1, gen2 = file.read().splitlines()
    
hamming_distance = sum(base1 != base2 for base1, base2 in zip(gen1, gen2))
print(hamming_distance)