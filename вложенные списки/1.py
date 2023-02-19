b = [int(i) for i in input().split()]
n = b[0]
m = b[1]
a = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    rez = [float(i) for i in input().split()]
    for j in range(m):
        a[i][j] = rez[j]
max = a[0][0]
x = 0
y = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
            x = i
            y = j
print(x, y)
