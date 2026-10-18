from collections import defaultdict


def parse_newick_to_graph(newick: str):
    graph = defaultdict(list)
    stack = []
    internal_id = 0
    i = 0

    def connect(a, b, weight):
        graph[a].append((b, weight))
        graph[b].append((a, weight))

    def read_label_and_weight():
        nonlocal i

        while i < len(newick) and newick[i].isspace():
            i += 1

        start = i
        while i < len(newick) and newick[i] not in ":,();":
            i += 1
        name = newick[start:i].strip()

        weight = 0
        if i < len(newick) and newick[i] == ":":
            i += 1
            start = i
            while i < len(newick) and newick[i] not in ",);":
                i += 1

            value = float(newick[start:i].strip())
            weight = int(value) if value.is_integer() else value

        return name, weight

    while i < len(newick):
        ch = newick[i]

        if ch.isspace() or ch == ",":
            i += 1

        elif ch == "(":
            stack.append("(")
            i += 1

        elif ch == ")":
            i += 1
            name, weight = read_label_and_weight()

            if not name:
                name = f"#{internal_id}"
                internal_id += 1

            graph[name] 

            while stack and stack[-1] != "(":
                child, child_weight = stack.pop()
                connect(name, child, child_weight)

            stack.pop() 
            stack.append((name, weight))

        elif ch == ";":
            break

        else:
            name, weight = read_label_and_weight()
            graph[name]
            stack.append((name, weight))

    return graph


def prepare(graph, root):
    parent = {root: None}
    depth = {root: 0}
    dist = {root: 0}
    stack = [root]

    while stack:
        v = stack.pop()

        for to, weight in graph[v]:
            if to in parent:
                continue

            parent[to] = v
            depth[to] = depth[v] + 1
            dist[to] = dist[v] + weight
            stack.append(to)

    return parent, depth, dist


def lca(a, b, parent, depth):
    while depth[a] > depth[b]:
        a = parent[a]

    while depth[b] > depth[a]:
        b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


def solve() -> None:
    with open("src/NKEW/input.txt", "r", encoding="utf-8") as f:
        data = [line.strip() for line in f if line.strip()]

    ans = []
    for i in range(0, len(data), 2):
        graph = parse_newick_to_graph(data[i])
        a, b = data[i + 1].split()
        parents, depths, dists = prepare(graph, next(iter(graph)))
        lca_v = lca(a, b, parents, depths)
        ans.append(str(dists[a] + dists[b] - 2 * dists[lca_v]))
        

    with open("src/NKEW/output.txt", "w", encoding="utf-8") as f:
        f.write(' '.join(ans))


if __name__ == "__main__":
    solve()
