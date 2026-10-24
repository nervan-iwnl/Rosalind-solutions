from collections import deque

class Node:
    def __init__(self, start=-1, end=0, suffix_start=None):
        self.start = start
        self.end = end

        self.children = {}
        self.link = None

        
        self.suffix_start = suffix_start


class SuffixTree:
    def __init__(self, text, terminal="$"):
        if len(terminal) != 1 or terminal in text:
            raise ValueError(
                "Terminator must be only one char "
                "that's not in text"
            )

        self.s = text + terminal

        self.root = Node()
        self.root.link = self.root

        self.pos = -1

        self.active_node = self.root
        self.active_edge = -1
        self.active_length = 0

        self.remainder = 0

        for i in range(len(self.s)):
            self._extend(i)
                
    def _new_node(self, start, end, suffix_start=None):
        node = Node(start, end, suffix_start)
        node.link = self.root
        return node
    
    def _edge_length(self, edge):
        if edge.end == None:
            end = self.pos + 1
        else:
            end = edge.end
        
        return end - edge.start
    
    def _extend(self, i):
        self.pos = i 
        
        self.remainder += 1
        
        last = None
        while self.remainder > 0:
            if self.active_length == 0:
                self.active_edge = i
                
            key = self.s[self.active_edge]
            nxt = self.active_node.children.get(key)
            if nxt is None:
                leaf = self._new_node(
                    i,
                    None,
                    suffix_start=i - self.remainder + 1, 
                )
                
                self.active_node.children[key] = leaf 
                
                if last is not None:
                    last.link = self.active_node
                    last = None
            else:
                length = self._edge_length(nxt)
                
                if self.active_length >= length:
                    self.active_edge += length
                    self.active_length -= length
                    self.active_node = nxt
                    continue
                
                nxt_chr = self.s[nxt.start + self.active_length]
                
                if self.s[i] == nxt_chr:
                    if ( 
                        last is not None and
                        self.active_node is not self.root
                    ):
                        last.link = self.active_node
                        
                    self.active_length += 1
                    break
                
                split = self._new_node(
                    start=nxt.start,
                    end=self.active_length + nxt.start,
                )
                self.active_node.children[key] = split
                
                leaf = self._new_node(
                    start=i,
                    end=None,
                    suffix_start=i - self.remainder + 1,
                )
                
                split.children[self.s[i]] = leaf
                nxt.start += self.active_length
                split.children[self.s[nxt.start]] = nxt
                
                if last is not None:
                    last.link = split
                    
                last = split
                
            self.remainder -= 1
            
            if (
                self.active_node is self.root 
                and self.active_length > 0
            ):
                self.active_length -= 1
                self.active_edge = (
                    i - self.remainder + 1
                )
            elif self.active_node is not self.root:
                self.active_node = self.active_node.link
            
    def __str__(self):
        q = deque([self.root])
        ans = []

        while q:
            node = q.popleft()

            for v in node.children.values():
                end = self.pos + 1 if v.end is None else v.end
                ans.append(self.s[v.start:end])
                q.append(v)

        return "\n".join(ans)


def solve() -> None:
    with open("src/SUFF/input.txt", "r", encoding="utf-8") as f:
        data = f.read().strip()

    result = SuffixTree(data.removesuffix("$"))

    with open("src/SUFF/output.txt", "w", encoding="utf-8") as f:
        f.write(str(result))


if __name__ == "__main__":
    solve()
