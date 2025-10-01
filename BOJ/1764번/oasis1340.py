count1, count2 = map(int, input().split())
names = set()
result = []

for i in range (count1):
  name = input()
  names.add(name)

for i in range (count2):
  name = input()
  if name in names:
    result.append(name)

result.sort()

print(len(result))

for i in range (len(result)):
  print(result[i])
