from collections import deque


def normalize(p, q):
    pos = {x: i + 1 for i, x in enumerate(q)}
    return tuple(pos[x] for x in p)


def neighbors(perm):
    n = len(perm)
    for l in range(n):
        for r in range(l + 1, n):
            yield perm[:l] + perm[l:r + 1][::-1] + perm[r + 1:]


def expand_layer(queue, dist_this, dist_other):
    layer_size = len(queue)

    for _ in range(layer_size):
        cur = queue.popleft()
        d = dist_this[cur]

        if cur in dist_other:
            return d + dist_other[cur]

        for nxt in neighbors(cur):
            if nxt in dist_this:
                continue

            dist_this[nxt] = d + 1

            if nxt in dist_other:
                return dist_this[nxt] + dist_other[nxt]

            queue.append(nxt)

    return None


def reversal_distance(p, q):
    start = normalize(p, q)
    target = tuple(range(1, len(p) + 1))

    if start == target:
        return 0

    q1 = deque([start])
    q2 = deque([target])

    d1 = {start: 0}
    d2 = {target: 0}

    while q1 and q2:
        if len(q1) <= len(q2):
            ans = expand_layer(q1, d1, d2)
        else:
            ans = expand_layer(q2, d2, d1)

        if ans is not None:
            return ans

    return -1


def parse_input(filename):
    pairs = []
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]

    for i in range(0, len(lines), 2):
        p = list(map(int, lines[i].split()))
        q = list(map(int, lines[i + 1].split()))
        pairs.append((p, q))

    return pairs


pairs = parse_input("./src/REAR/input.txt")
ans = [reversal_distance(p, q) for p, q in pairs]

with open('./src/REAR/output.txt', 'w') as f:
    f.write(' '.join(map(str, ans)))