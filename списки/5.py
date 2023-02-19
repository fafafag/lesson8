n = 0
x = list(map(int, input().split()))
for i in range(1, (len(x)-1)):
    if x[i-1] < x[i] and x[i] > x[i+1]:
        n += 1
print(n)
