with open("./src/FIB/input.txt", "r") as file:
    line = file.read()
n, k = map(int, line.split())

arr = [1, 1]

for i in range(2, n):
    next_value = arr[i - 2] * k + arr[i - 1]
    arr.append(next_value)
    
print(arr[n - 1])