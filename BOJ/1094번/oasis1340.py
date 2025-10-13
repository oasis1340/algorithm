from itertools import combinations

x = int(input())
count = list()

for i in range(1, 65):
  if 64 % i == 0:
    count.append(i)

for i in range(1, len(count) + 1):
  found = False
  for num in combinations(count, i):
    if sum(num) == x:
      print(len(num))
      found = True
      break
  if found:
    break
