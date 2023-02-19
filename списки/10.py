a = list(map(int, input().split()))

min = a[0]
max = a[0]
pos_min = 0
pos_max = 0

for i in range(0, len(a)):
    if min > a[i]:
        min = a[i]
        pos_min = i
    if max < a[i]:
        max = a[i]
        pos_max = i

a[pos_min] = max
a[pos_max] = min

for i in range(0, len(a)):
    print(a[i])
