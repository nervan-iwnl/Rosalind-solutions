with open("./src/SETO/input.txt", "r") as f:
    n = int(f.readline().strip())
    line1 = f.readline().strip()
    line2 = f.readline().strip()

def parse_set(s: str) -> set[int]:
    s = s.strip()[1:-1] 
    if not s:
        return set()
    return set(map(int, s.split(",")))

a = parse_set(line1)
b = parse_set(line2)

ALL = set(range(1, n + 1))

with open('./src/SETO/output.txt', 'w') as f:
    f.write(f'{a | b}\n')
    f.write(f'{a & b}\n')
    f.write(f'{a - b}\n')
    f.write(f'{b - a}\n')
    f.write(f'{ALL - a}\n')
    f.write(f'{ALL - b}\n')