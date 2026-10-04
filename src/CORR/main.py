def read_fasta(path):
    seqs, cur = [], []
    for line in open(path):
        if line[0] == '>':
            if cur: seqs.append(''.join(cur)); cur = []
        else:
            cur.append(line.strip())
    if cur: seqs.append(''.join(cur))
    return seqs


def solve() -> None:
    data = read_fasta("src/CORR/input.txt")
    complement = str.maketrans("ACGT", "TGCA")
    el_cnt = {}
    solo_els = set()

    for el in data:
        rev = el.translate(complement)[::-1]
        if el in el_cnt:
            el_cnt[el] += 1
            solo_els.discard(el)
        elif rev in el_cnt:
            el_cnt[rev] += 1
            solo_els.discard(rev)
        else:
            el_cnt[el] = 1
            solo_els.add(el)

    with open("src/CORR/output.txt", "w", encoding="utf-8") as f:
        for el in solo_els:
            found = False

            for idx in range(len(el)):
                for ch in "ATCG":
                    if ch == el[idx]:
                        continue

                    s = el[:idx] + ch + el[idx + 1:]
                    rev = s.translate(complement)[::-1]

                    if el_cnt.get(s, 0) > 1 or el_cnt.get(rev, 0) > 1:
                        f.write(f"{el}->{s}\n")
                        found = True
                        break

                if found:
                    break
                
                
if __name__ == "__main__":
    solve()