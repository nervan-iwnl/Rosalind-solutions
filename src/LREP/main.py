from collections import defaultdict
from collections import deque

def solve() -> None:
    tree = defaultdict(list)
    parents = set()
    children = set()

    with open("src/LREP/input.txt", "r", encoding="utf-8") as f:
        inp = f.readline().strip()
        k = int(f.readline())
        for line in f.readlines():
            if not line.strip():
                continue 
            
            parent, child, start, length = line.split()
            start = int(start) - 1  
            length = int(length)

            tree[parent].append((child, start, length))
            parents.add(parent)
            children.add(child)

        root = (parents - children).pop()
        max_ans = inp.removesuffix("$") if k == 1 else ""
        def dfs(node, substr):
            nonlocal max_ans

            if not tree[node]:
                return 1

            count = sum(dfs(child, substr + inp[start:start + length]) for child, start, length in tree[node])
            if count >= k and len(substr) > len(max_ans):
                max_ans = substr

            return count
        
        dfs(root, "")
    
    with open("src/LREP/output.txt", "w", encoding="utf-8") as f:
        f.write(max_ans)


if __name__ == "__main__":
    solve()
