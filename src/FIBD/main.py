with open("./src/FIBD/input.txt", "r") as file:
    line = file.read()
n, m = map(int, line.split())

arr = [0, 1, 1]
for i in range(3, n + 1):
    arr.append((arr[i - 1] + arr[i - 2]))
    if i == m + 1:
        arr[i] -= 1
    elif i > m + 1:
        arr[i] -= arr[i - m - 1]
        
print(arr[n])