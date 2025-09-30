count = int(input())
a = []

for i in range(count):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: (x[0], x[1]))

for i in range(count):
    print(a[i][0], a[i][1])
