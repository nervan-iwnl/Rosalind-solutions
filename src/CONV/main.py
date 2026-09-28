def solve() -> None:
    with open("src/CONV/input.txt", "r", encoding="utf-8") as f:
        data = f.readlines()
        m1 = [float(i) for i in data[0].split()]
        m2 = [float(i) for i in data[1].split()]
        
    ans = {}
    
    for el1 in m1:
        for el2 in m2:
            tmp = round(el1 - el2, 6)
            ans[tmp] = ans.get(tmp, 0) + 1
    
    print(ans)
    ans_cnt = max(ans.values())
    cnt = 0
    for k, v in ans.items():
        if v == ans_cnt:
            cnt = k
            break        
    result = (ans_cnt, cnt)

    with open("src/CONV/output.txt", "w", encoding="utf-8") as f:
        f.write(str(result[0]) + '\n' + str(result[1]))


if __name__ == "__main__":
    solve()
