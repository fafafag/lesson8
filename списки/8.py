a = input().split()
a = list(map(int, a))
x = a[0]
s = 1

for i in range(0, len(a)):
    if x != a[i]:
        s = s + 1
        x = a[i]
print(s)
