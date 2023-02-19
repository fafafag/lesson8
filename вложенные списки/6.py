def swap_columns(a, i, j):
    for row in range(len(a)):
        a[row][i], a[row][j] = a[row][j], a[row][i]
    for row in a:
        print(" ".join([str(i) for i in row]))


n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(l) for l in input().split()]

swap_columns(a, i, j)