a = list(map(int, input().split()))
x = 0

for i in range(0, len(a), 2):
    if i + 1 < len(a):
        x = a[i]
        a[i] = a[i + 1]
        a[i + 1] = x
        print(a[i])
        print(a[i + 1])
    else:
        print(a[i])
