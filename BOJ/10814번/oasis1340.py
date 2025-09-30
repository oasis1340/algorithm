count = int(input())
human = []

for i in range(count):
  age, name = input().split()
  human.append((int(age), name))

human.sort(key=lambda x: x[0])

for i in range(count):
    print(human[i][0], human[i][1])
