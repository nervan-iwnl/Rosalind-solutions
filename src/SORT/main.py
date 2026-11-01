from collections import deque

visited = set()
parent = {}
queue = deque()

def bfs(current):
    n = len(current)
    for l in range(n):
        for r in range(l + 1, n):
            neighbor = (
                current[:l]
                + current[l:r + 1][::-1]
                + current[r + 1:]
            )

            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = (current, (l + 1, r + 1))
                queue.append(neighbor)


def solve() -> None:
    with open("src/SORT/input.txt", "r", encoding="utf-8") as f:
        start = tuple(map(int, f.readline().split()))
        target = tuple(map(int, f.readline().split()))

    visited.clear()
    parent.clear()
    queue.clear()

    visited.add(start)
    queue.append(start)

    while queue:
        current = queue.popleft()

        if current == target:
            break

        bfs(current)

    operations = []
    current = target

    while current != start:
        previous, reversal = parent[current]
        operations.append(reversal)
        current = previous

    operations.reverse()

    with open("src/SORT/output.txt", "w", encoding="utf-8") as f:
        f.write(str(len(operations)) + "\n")
        for l, r in operations:
            f.write(f"{l} {r}\n")


if __name__ == "__main__":
    solve()
