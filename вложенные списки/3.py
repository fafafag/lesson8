b = [int(i) for i in input().split()]
n = b[0]
m = b[1]

a = [['*'] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if (i+j) % 2 == 0:
            a[i][j] = '.'
for row in a:
    print(' '.join([str(elem) for elem in row]))