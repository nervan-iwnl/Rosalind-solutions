from typing import List
import bisect

def lis(arr: List) -> List:
    tails = []
    tails_idx = []
    parents = []
    for i, el in enumerate(arr):
        idx = bisect.bisect_left(tails, el)
        if idx == len(tails):
            tails.append(el)
            tails_idx.append(i)
        else:
            tails[idx] = el
            tails_idx[idx] = i
    
        if idx > 0:
            parents.append(tails_idx[idx - 1])
        else: 
            parents.append(-1)
            
    ans = []
    pos = tails_idx[-1] if tails_idx else -1
    while pos != -1:
        ans.append(arr[pos])
        pos = parents[pos]
    
    return ans[::-1]


with open('./src/LGIS/input.txt') as f:
    f.readline()
    arr = [int(i) for i in f.readline().split()]
    

with open('./src/LGIS/output.txt', 'w') as f:
    f.write(' '.join([str(i) for i in lis(arr)]))
    f.write('\n')
    f.write(' '.join([str(i) for i in lis(arr[::-1])[::-1]]))
    
