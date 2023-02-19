a = input().split()
a = list(map(int, a))
x = int(input())
s = len(a) + 1

for i in range(0, len(a)):
    if x > a[i]:
        s = i + 1
        break
print(s)
