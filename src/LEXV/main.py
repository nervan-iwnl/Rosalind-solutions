with open("./src/LEXV/input.txt") as f:
    alph = f.readline().strip().split()
    n = int(f.readline().strip())
    


ans = []
def gen(curr):
    if len(curr) == n:
        return
    
    for c in alph:
        ans.append(curr + c)
        gen(curr + c)


gen("")
with open("./src/LEXV/output.txt", "w") as f:
    f.write("\n".join(ans))