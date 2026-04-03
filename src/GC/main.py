with open("./src/GC/input.txt", "r") as file:
    content = file.read()

arr = {}

for line in content.splitlines():
    if line.startswith(">") or not line.strip():
        arr[line[1:]] = ""
    else:
        arr[list(arr.keys())[-1]] += line.strip()

max_gc_key = ""
max_gc_content = 0
for key in arr:
    gc_count = sum(1 for nucleotide in arr[key] if nucleotide in "GC")
    gc_content = (gc_count / len(arr[key])) * 100
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_key = key

print(f"{max_gc_key}\n{max_gc_content}")