from collections import deque

with open("./src/TREE/input.txt") as f:
    arr = f.readlines()
    
n = int(arr[0])
arr = [[int(i) for i in line.split()] for line in arr[1:]]

graph = [[] for _ in range(n)]
for a, b in arr:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
    


comp = 0
visited = [False] * n
for i in range(n):
    if visited[i]:
        continue
    q = deque()
    q.append(i)
    while len(q) > 0:
        cur = q[-1]
        q.pop()
        if visited[cur]: 
            continue
        visited[cur] = True
        for adj in graph[cur]:
            q.append(adj)
    
    comp += 1
    
with open("./src/TREE/output.txt", 'w') as f:
    f.write(f'{comp - 1}')