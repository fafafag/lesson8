data = [int(i) for i in input().split()]
# Index, Element
k, c = [int(i) for i in input().split()]
data.insert(k, c)
for i in data:
        print(i, end=" ")
