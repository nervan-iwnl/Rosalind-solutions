from collections import defaultdict

LEAF_PROBABILITIES = {
    "AA": (1.0, 0.0, 0.0),
    "Aa": (0.0, 1.0, 0.0),
    "aa": (0.0, 0.0, 1.0),
}

def parse_newick_to_graph(newick: str):
    graph = defaultdict(list)
    stack = []
    token = ""
    internal_id = 0
    last_closed = None 

    def connect(a, b):
        graph[a].append(b)

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

    return graph, stack[-1]

def dfs(graph, v):
    if v in LEAF_PROBABILITIES:
       return LEAF_PROBABILITIES[v]

    l, r = graph[v]
    
    left, right = graph[v]
    left_AA, left_Aa, _ = dfs(graph, left)
    right_AA, right_Aa, _ = dfs(graph, right)

    p = left_AA + left_Aa / 2
    q = right_AA + right_Aa / 2

    return (
        p * q,
        p * (1 - q) + (1 - p) * q,
        (1 - p) * (1 - q),
    )

    
   

def solve() -> None:
    with open("src/MEND/input.txt", "r", encoding="utf-8") as f:
        graph, root = parse_newick_to_graph(f.read().strip())

    result = dfs(graph, root)
    
    with open("src/MEND/output.txt", "w", encoding="utf-8") as f:
        print(*result, file=f)


if __name__ == "__main__":
    solve()
