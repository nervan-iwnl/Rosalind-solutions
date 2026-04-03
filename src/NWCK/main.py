from collections import defaultdict, deque

with open("./src/NWCK/input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

tests = []
for i in range(0, len(lines), 2):
    newick = lines[i]
    x, y = lines[i + 1].split()
    tests.append((newick, x, y))


    
def parse_newick_to_graph(newick: str):
    graph = defaultdict(list)
    stack = []
    token = ""
    internal_id = 0
    last_closed = None 

    def connect(a, b):
        graph[a].append(b)
        graph[b].append(a)

    def rename_last_closed(name):
        nonlocal last_closed
        old = last_closed
        if old is None:
            stack.append(name)
            return

        for nei in graph[old]:
            graph[nei].remove(old)
            graph[nei].append(name)
            graph[name].append(nei)

        del graph[old]

        if stack and stack[-1] == old:
            stack[-1] = name

        last_closed = name

    for ch in newick:
        if ch.isalnum() or ch == '_':
            token += ch

        elif ch == '(':
            stack.append('(')
            last_closed = None

        elif ch == ',':
            if token:
                if last_closed is not None:
                    rename_last_closed(token)
                else:
                    stack.append(token)
                token = ""
            last_closed = None

        elif ch == ')':
            if token:
                if last_closed is not None:
                    rename_last_closed(token)
                else:
                    stack.append(token)
                token = ""

            children = []
            while stack and stack[-1] != '(':
                children.append(stack.pop())
            stack.pop() 

            parent = f"#{internal_id}"
            internal_id += 1

            for child in children:
                connect(parent, child)

            stack.append(parent)
            last_closed = parent

        elif ch == ';':
            if token:
                if last_closed is not None:
                    rename_last_closed(token)
                else:
                    stack.append(token)
                token = ""

    return graph



def bfs(graph, x, y):
    q = deque([(x, 0)])
    visited = {x}

    while q:
        node, dist = q.popleft()

        if node == y:
            return dist

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))


ans = []
for newick, x, y in tests:
    ans.append(str(bfs(parse_newick_to_graph(newick), x, y)))
    print(parse_newick_to_graph(newick))
    
with open('./src/NWCK/output.txt', 'w') as f:
    f.write(' '.join(ans))