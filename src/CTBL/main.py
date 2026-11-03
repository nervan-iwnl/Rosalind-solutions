from collections import defaultdict


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


def build_character_table(graph):
    taxa = sorted(node for node in graph if len(graph[node]) == 1)
    taxon_set = set(taxa)
    rows = []

    for a in graph:
        for b in graph[a]:
            if a >= b:
                continue

            visited = {a, b}
            stack = [a]
            side = set()

            while stack:
                node = stack.pop()
                if node in taxon_set:
                    side.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            if 2 <= len(side) <= len(taxa) - 2:
                row = "".join("1" if taxon in side else "0" for taxon in taxa)
                rows.append(row)

    return rows


def solve() -> None:
    with open("src/CTBL/input.txt", "r", encoding="utf-8") as f:
        data = f.read()

    graph = parse_newick_to_graph(data)


    with open("src/CTBL/output.txt", "w", encoding="utf-8") as f:
        for row in build_character_table(graph):
            f.write(f'{row}\n')


if __name__ == "__main__":
    solve()
